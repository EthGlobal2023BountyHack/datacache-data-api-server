"""datacache_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import os

from datacache.views import *

TITLE = os.getenv("ADMIN_TITLE", default="DataCache")

admin.site.site_header = TITLE
admin.site.index_title = TITLE
admin.site.site_title = TITLE

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/wallet/tag/add/', AddTagToWalletView.as_view(), name='add_wallet_tag'),
    path('api/wallet/add/', AddWalletView.as_view(), name='add_wallet'),
    path('api/wallet/tag/list/', WalletTagListView.as_view(), name='list_wallet_tag'),
    path('api/tag/list/', TagListView.as_view(), name='list_tag'),
]
