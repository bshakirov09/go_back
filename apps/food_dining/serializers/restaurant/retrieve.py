# Rest-Framework
from rest_framework import serializers

# Project
from file.models import File
from file.serializers import FileSerializer
from food_dining.models import (
    Restaurant,
    ItHas,
    FoodType,
    ServiceOption,
    WorkingHours,
    OrderSiteLink,
    ReserveSiteLink
)


class RestaurantSerializer(serializers.ModelSerializer):
    it_has = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()
    is_favorite = serializers.SerializerMethodField()
    review = serializers.SerializerMethodField()
    working_days = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name',
            'type_model',
            'it_has',
            'files',
            'is_favorite',
            'review',
            'latitude',
            'longitude',
            'please_note',
            'working_days'
        ]

    def get_it_has(self, obj):
        return ItHas.objects.filter(restauranthas__restaurant=obj).values('name')

    def get_files(self, obj):
        file = File.objects.filter(restaurantmedia__restaurant=obj, is_main=True).first()
        if file is not None:
            return FileSerializer(file, context=self.context).data
        return None

    def get_working_days(self, obj):
        return

    def get_is_favorite(self, obj):  # TODO FIX
        return False

    def get_review(self, obj):  # TODO FIX
        return 5


class RestaurantDetailSerializer(serializers.ModelSerializer):
    food_types = serializers.SerializerMethodField()
    service_options = serializers.SerializerMethodField()
    it_has = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()
    working_days = serializers.SerializerMethodField()
    order_sites = serializers.SerializerMethodField()
    reserve_sites = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name',
            'phone_number',
            'website',
            'type_model',
            'latitude',
            'longitude',
            'please_note',
            'twitter_url',
            'instagram_url',
            'facebook_url',
            'country',
            'city',
            'food_types',
            'service_options',
            'it_has',
            'files',
            'working_days',
            'order_sites',
            'reserve_sites'
        ]

    def get_food_types(self, obj):
        return FoodType.objects.filter(restaurantfoodtype__restaurant=obj).values('id', 'name')

    def get_service_options(self, obj):
        return ServiceOption.objects.filter(restaurantserviceoption__restaurant=obj).values('id', 'name')

    def get_it_has(self, obj):
        return ItHas.objects.filter(restauranthas__restaurant=obj).values('name')

    def get_working_days(self, obj):
        return WorkingHours.objects.filter(restaurantworkingdays__restaurant=obj).values(
            'id',
            'start_time',
            'end_time',
            'week_day',
            'is_holiday'
        )

    def get_files(self, obj):
        files = File.objects.filter(restaurantmedia__restaurant=obj).order_by('ordering')
        if not files:
            return FileSerializer(files, many=True, context=self.context).data
        return None

    def get_order_sites(self, obj):
        return OrderSiteLink.objects.filter(restaurantordersite__restaurant=obj).values('id', 'name')

    def get_reserve_sites(self, obj):
        return ReserveSiteLink.objects.filter(restaurantreservesite__restaurant=obj).values('id', 'name')
