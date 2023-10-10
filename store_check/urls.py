from django.urls import path

from store_check.apps import StoreCheckConfig
from store_check.views import StoreListAPIView, VisitCreateAPIView

app_name = StoreCheckConfig.name

urlpatterns = [
    path('stores/', StoreListAPIView.as_view(), name='stores'),
    path('stores/create-visit/', VisitCreateAPIView.as_view(), name='create-visit'),
]
