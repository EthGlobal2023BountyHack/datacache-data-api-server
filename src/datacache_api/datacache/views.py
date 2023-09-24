from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.db.models import Q
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

class TagListView(View):
    def get(self, request, *args, **kwargs):
        query = Tag.objects.all()
        res = list()
        for cell in query:
            res.append({"id": cell.id, "name": cell.name})
        return JsonResponse({'status': 0, 'message': 'Success', "list": res})

class WalletTagListView(View):
    def get_tag_data(self, user):
        tags = user.tags.all()
        tag_data_list = []
        for tag in tags:
            tag_data = {
                "id": tag.id,
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

class FetchUsersByTags(View):
    def get(self, request, *args, **kwargs):
        tags = request.GET.get('tags')
        condition = request.GET.get('condition', 'or').lower() 
        if not tags:
            return error('Invalid data')
        try:
            tag_ids = [int(x) for x in tags.split(",")]
        except ValueError:
            return error('Invalid tag IDs')
        if condition == 'and':
            user_sets = [set(UserTags.objects.filter(tag__id=tag_id).values_list('user_data__wallet_address', flat=True)) for tag_id in tag_ids]
            common_users = set.intersection(*user_sets)
        else:
            q_objects = Q()
            for tag_id in tag_ids:
                q_objects |= Q(tag__id=tag_id)
            user_tags = UserTags.objects.filter(q_objects).select_related('user_data').distinct()
            common_users = {user_tag.user_data.wallet_address for user_tag in user_tags}
        
        res = [{"address": address} for address in common_users]

        return JsonResponse({'status': 0, 'message': 'Success', 'list': res, 'count': len(res)})
