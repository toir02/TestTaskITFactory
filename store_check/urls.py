from django.urls import path

from store_check.apps import StoreCheckConfig
from store_check.views import StoreListAPIView

app_name = StoreCheckConfig.name

urlpatterns = [
    path('stores/', StoreListAPIView.as_view(), name='stores')
]
