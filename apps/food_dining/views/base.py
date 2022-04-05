# Rest-Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import UpdateModelMixin

# Project
from food_dining.models import (
    FoodType,
    ServiceOption,
    ItHas,
    GoodFor,
    OrderSiteLink,
    ReserveSiteLink,
    WorkingHours
)
from food_dining.serializers.base import (
    FoodTypeSerializer,
    ServiceOptionSerializer,
    ItHasSerializer,
    GoodForSerializer,
    OrderSiteSerializer,
    ReserveSiteSerializer,
    WorkingHoursSerializer
)


class FoodTypeViewSet(ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer


class ServiceOptionViewSet(ModelViewSet):
    queryset = ServiceOption.objects.all()
    serializer_class = ServiceOptionSerializer


class ItHasViewSet(ModelViewSet):
    queryset = ItHas.objects.all()
    serializer_class = ItHasSerializer


class GoodForViewSet(ModelViewSet):
    queryset = GoodFor.objects.all()
    serializer_class = GoodForSerializer


class OrderSiteViewSet(ModelViewSet):
    queryset = OrderSiteLink.objects.all()
    serializer_class = OrderSiteSerializer


class ReserveSiteViewSet(ModelViewSet):
    queryset = ReserveSiteLink.objects.all()
    serializer_class = ReserveSiteSerializer


class WorkingHoursUpdate(GenericViewSet, UpdateModelMixin):
    queryset = WorkingHours.objects.all()
    serializer_class = WorkingHoursSerializer
