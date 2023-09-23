from django.contrib import admin
from django import forms
from .models import *

from flat_json_widget.widgets import FlatJsonWidget

class AirstackConfigForm(forms.ModelForm):
    class Meta:
        widgets = {
            'variables': FlatJsonWidget,
            'filter_variables': FlatJsonWidget
        }

@admin.register(AirstackConfig)
class AirstackConfigAdmin(admin.ModelAdmin):
    list_display = ('tag', 'desc', 'tag', )
    search_fields = ('desc', )
    list_filter = ('detached', 'tag', )
    form = AirstackConfigForm


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'origin',  )
    search_fields = ('name', 'origin', )
    list_filter = ('detached', 'origin', )


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ('wallet_address', 'tags_content' )
    search_fields = ('wallet_address', )
    list_filter = ('tags', 'detached', )


@admin.register(UserTags)
class UserTagsAdmin(admin.ModelAdmin):
    list_display = ('user_data', 'tag', 'created', 'updated' )
    list_filter = ('tag', )
