from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .models import *

def success():
    return JsonResponse({'status': 0, 'message': 'Success'})

def error(msg, errcode=1):
    return JsonResponse({'status': errcode, 'message': msg})

class AddTagToWalletView(View):
    def post(self, request, *args, **kwargs):
        address = request.POST.get('address')
        tag = request.POST.get('tag')
        if not address or not tag:
            return error('Invalid data')
        user =  UserData.objects.get_user(address)
        tag = Tag.objects.get(id(tag))
        user.tags.add(self.tag)
        return success()

class AddWalletView(View):
    def post(self, request, *args, **kwargs):
        address = request.POST.get('address')
        if not address:
            return error('Invalid data')
        UserData.objects.get_user(address)
        # TODO: Async user tags
        UnSyncWallet.objects.get_or_create(address)
        response_data = {'status': 0, 'error': 'Success'}
        return success()

class WalletTagListView(View):
    def get_tag_data(self, user):
        tags = user.tags.all()
        tag_data_list = []
        for tag in tags:
            tag_data = {
                "name": tag.name,
                "origin": tag.origin,
                "updated": tag.updated.strftime('%Y-%m-%d %H:%M:%S'),  # assuming `updated` is a datetime field
            }
            tag_data_list.append(tag_data)
        return tag_data_list

    def get(self, request, *args, **kwargs):
        address = request.GET.get('address')
        if not address:
            return error('Invalid data')
        user =  UserData.objects.get_user(address)
        tag_data = self.get_tag_data(user)
        return JsonResponse({'status': 0, 'message': 'Success', "list": tag_data})