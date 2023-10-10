from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from store_check.models import Store, Visit
from store_check.serializers import StoreSerializer, VisitSerializer


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


class VisitCreateAPIView(generics.CreateAPIView):
    serializer_class = VisitSerializer
    queryset = Visit.objects.all()

    def perform_create(self, serializer):
        phone_number = self.request.query_params.get('phone_number')
        store_pk = self.request.data.get('store_pk')
        latitude = self.request.data.get('latitude')
        longitude = self.request.data.get('longitude')

        store = get_object_or_404(Store, pk=store_pk)

        if store.employee.phone_number != phone_number:
            raise ValidationError("Номер телефона не соответствует указанной торговой точке.")

        serializer.save(latitude=latitude, longitude=longitude, store=store)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response
