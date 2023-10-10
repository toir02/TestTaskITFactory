from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from store_check.models import Store
from store_check.serializers import StoreSerializer


class StoreListAPIView(generics.ListAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('employee__phone_number',)

    def get_queryset(self):
        queryset = super().get_queryset()
        phone_number = self.request.query_params.get('employee__phone_number')

        if not phone_number:
            return queryset.none()

        return queryset
