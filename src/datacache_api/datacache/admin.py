from django.contrib import admin
from django import forms
from .models import *
from django.urls import path
from django.shortcuts import render, redirect
from flat_json_widget.widgets import FlatJsonWidget
from django.urls import reverse

class AirstackConfigForm(forms.ModelForm):
    class Meta:
        widgets = {
            'variables': FlatJsonWidget,
            'filter_variables': FlatJsonWidget
        }

class UserTagsInline(admin.TabularInline):
    model = UserTags
    extra = 1 

@admin.register(TheGraphConfig)
class TheGraphConfigAdmin(admin.ModelAdmin):
    list_display = ('tag', 'desc', )
    search_fields = ('desc', )
    list_filter = ('detached', 'tag', )


@admin.register(AirstackConfig)
class AirstackConfigAdmin(admin.ModelAdmin):
    list_display = ('tag', 'desc', 'sync_button', )
    search_fields = ('desc', )
    list_filter = ('detached', 'tag', )
    form = AirstackConfigForm

    def sync_button(self, obj):
        url = reverse('admin:sync_tags', args=[obj.id])
        return format_html(
            '<button onclick="syncTagsForId(event, \'{}\')">Sync</button>',
            url
        )
    sync_button.short_description = 'Sync Action'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'sync_tags/<int:config_id>/',
                self.admin_site.admin_view(self.sync_tags_view),
                name='sync_tags',
            ),
        ]
        return custom_urls + urls

    def sync_tags_view(self, request, config_id):
        config = AirstackConfig.objects.get(id=config_id)
        config.create_tags()
        self.message_user(request, "Tags synced successfully.")
        return JsonResponse({"success": True})
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [UserTagsInline]
    list_display = ('id', 'name', 'origin',  )
    search_fields = ('name', 'origin', )
    list_filter = ('detached', 'origin', )


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    inlines = [UserTagsInline]
    list_display = ('wallet_address', 'tags_content' )
    search_fields = ('wallet_address', )
    list_filter = ('tags', 'detached', )


@admin.register(UserTags)
class UserTagsAdmin(admin.ModelAdmin):
    list_display = ('user_data', 'tag', 'created', 'updated' )
    list_filter = ('tag', )


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'boardcast', 'receiver', 'created', 'updated' )
    list_filter = ('boardcast', )
