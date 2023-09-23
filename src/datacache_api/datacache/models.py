from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils.html import format_html
from .constants import FILTER_TYPE_CHOICES, FILTER_TYPE
from .api import airstack_query
from jsonpath_ng import jsonpath, parse
import asyncio

# class DataUser(AbstractUser):
#     wallet_address = models.CharField(max_length=255, default='', blank=True, db_index=True)
class BaseModel(models.Model):
    detached = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def edit(self):
        return format_html('<a href="%d/change">Options</a>' % (self.id))
    edit.short_description = "Edit"

    class Meta:
        abstract = True

class TagManager(models.Manager):
    pass

class Tag(BaseModel):
    name = models.CharField('Name', max_length=100, default='', blank=True)
    origin = models.CharField('Origin', max_length=100, default='', blank=True)

    def __str__(self):
        return str(self.name)

class AirstackManager(models.Manager):
    pass

class AirstackConfig(BaseModel):
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING, null=True, related_name='airstack_config', verbose_name='Tag')
    desc = models.TextField('Description', default='', blank=True)
    query = models.TextField('Query', default='', blank=True)
    variables = models.JSONField('Variables', default=dict, blank=True)
    expression = models.CharField('Expression', max_length=255, default='', blank=True)
    limit = models.IntegerField('Limit Pages', default=1000, blank=True)
    support_list_result = models.BooleanField("Support List Result", default=True)
    objects = AirstackManager()

    def __str__(self):
        return str(self.tag.name)

    def create_tags(self):
        if not self.support_list_result:
            return
        data = asyncio.run(airstack_query(self.query, self.variables, self.limit))
        for query in data:
            exp = parse(self.expression)
            for match in exp.find(query):
                wallet_address = str(match.value)
                user = UserData.objects.get_user(wallet_address)
                user.tags.add(self.tag)

    def create_tag_from_user(self, wallet_address):
        if self.support_list_result:
            user_query = self.query.replace(
                'filter: {',
                'filter: { owner: {_eq: $identity},'
            ).replace(
                'query MyQuery {',
                'query MyQuery($identity: Identity) {'
            )
        else:
            user_query = self.query
        user_variables = self.variables.copy()
        user_variables['identity'] = wallet_address
        data = asyncio.run(airstack_query(user_query, user_variables, 1))
        for query in data:
            exp = parse(self.expression)
            for match in exp.find(query):
                print(match.value)
                wallet_address = str(match.value)
                user = UserData.objects.get_user(wallet_address)
                user.tags.add(self.tag)

class UserDataManager(models.Manager):
    def get_user(self, wallet_address):
        user, created = self.get_or_create(wallet_address=wallet_address)
        return user

class UserData(BaseModel):
    wallet_address = models.CharField(max_length=255, default='', blank=True, db_index=True)
    tags = models.ManyToManyField(
        Tag,
        through='UserTags',
        through_fields=('user_data', 'tag'),
        verbose_name='Tags', blank=True, null=True
    )
    objects = UserDataManager()
    
    def tags_content(self):
        return list(map(lambda x:x.name, self.tags.all()))
    tags_content.short_description = "Tags"

    def __str__(self):
        return self.wallet_address
    
class UserTags(BaseModel):
    user_data = models.ForeignKey(UserData, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_data) + " " + str(self.tag)
