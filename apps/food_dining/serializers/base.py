# Rest-Framework
from rest_framework import serializers

# Models
from file.models import File
from food_dining.models import (
    FoodType,
    ServiceOption,
    ItHas,
    GoodFor,
    OrderSiteLink,
    ReserveSiteLink,
    WorkingHours
)


class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ['id', 'name', ]


class ServiceOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOption
        fields = ['id', 'name', ]


class ItHasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItHas
        fields = ['id', 'name', ]


class GoodForSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodFor
        fields = ['id', 'name', ]


class OrderSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSiteLink
        fields = ['id', 'name']


class ReserveSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReserveSiteLink
        fields = ['id', 'name']


class WorkingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingHours
        fields = [
            'id',
            'start_time',
            'end_time',
            'week_day',
            'is_holiday'
        ]
        extra_kwargs = {
            'week_day': {'read_only': True},
        }


# Base Food Dining serializer
class BaseFoodDiningSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=35)
    website = serializers.CharField()
    latitude = serializers.CharField()
    longitude = serializers.CharField()
    please_note = serializers.CharField(required=False, default=None, allow_null=True, allow_blank=True)
    twitter_url = serializers.CharField(required=False, default=None, allow_null=True, allow_blank=True)
    facebook_url = serializers.CharField(required=False, default=None, allow_null=True, allow_blank=True)
    instagram_url = serializers.CharField(required=False, default=None, allow_null=True, allow_blank=True)
    country = serializers.CharField()
    city = serializers.CharField()


# Base Select serializers
class ItHasSelectSerializer(serializers.Serializer):
    it_has = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=ItHas.objects.all())
    )


class GodForSelectSerializer(serializers.Serializer):
    good_for = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=GoodFor.objects.all())
    )


class FoodTypeSelectSerializer(serializers.Serializer):
    food_type = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=FoodType.objects.all())
    )


class ServiceOptionSelectSerializer(serializers.Serializer):
    service_option = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=ServiceOption.objects.all())
    )


class MediaSelectSerializer(serializers.Serializer):
    files = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=File.objects.all())
    )


class OrderSiteSelectSerializer(serializers.Serializer):
    order_sites = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=OrderSiteLink.objects.all())
    )


class ReserveSiteSelectSerializer(serializers.Serializer):
    reserve_sites = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=ReserveSiteLink.objects.all())
    )
