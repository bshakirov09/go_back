# Rest-Framework
from rest_framework import serializers

# Project
from file.models import File
from file.serializers import FileSerializer

from food_dining.models.base_model import (
    TypeModel,
    ItHas,
    FoodType,
    GoodFor,
    ServiceOption,
    OrderSiteLink,
    ReserveSiteLink,
    WorkingHours
)
from food_dining.models import FoodService, FoodServiceMeal, FoodServiceMenu
from food_dining.serializers.base import BaseFoodDiningSerializer


class FoodServiceCreateSerializer(BaseFoodDiningSerializer):
    type_model = serializers.ChoiceField(choices=TypeModel.choices)
    it_has = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=ItHas.objects.all())
    )
    good_for = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=GoodFor.objects.all())
    )
    food_type = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=FoodType.objects.all())
    )
    service_option = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=ServiceOption.objects.all())
    )
    files = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=File.objects.all())
    )
    order_sites = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=OrderSiteLink.objects.all())
    )
    reserve_sites = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=ReserveSiteLink.objects.all())
    )


class FoodServiceUpdateSerializer(BaseFoodDiningSerializer):
    type_model = serializers.ChoiceField(choices=TypeModel.choices)


