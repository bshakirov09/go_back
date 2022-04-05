# Rest-Framework
from rest_framework import serializers

# Project
from file.models import File
from file.serializers import FileSerializer
from food_dining.models.base_model import (
    TypeModel,
    ItHas,
    FoodType,
    ServiceOption,
    OrderSiteLink,
    WorkingHours
)
from food_dining.models.take_out import TakeOutMenu, TakeOutMeal, TakeOut
from food_dining.serializers.base import BaseFoodDiningSerializer


class TakeOutCreateSerializer(BaseFoodDiningSerializer):
    type_model = serializers.ChoiceField(choices=TypeModel.choices)
    it_has = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=ItHas.objects.all())
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


class TakeOutUpdateSerializer(BaseFoodDiningSerializer):
    type_model = serializers.ChoiceField(choices=TypeModel.choices)


class TakeOutMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakeOutMenu
        fields = [
            'id',
            'name',
            'take_out'
        ]


class TakeOutMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakeOutMeal
        fields = [
            'id',
            'menu',
            'name',
            'price',
            'description',
            'photo'
        ]

    def to_representation(self, instance):
        self.fields['menu'] = TakeOutMenuSerializer()
        self.fields['photo'] = FileSerializer(context=self.context)
        return super(TakeOutMealSerializer, self).to_representation(instance)


class TakeOutSerializer(serializers.ModelSerializer):
    it_has = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()
    is_favorite = serializers.SerializerMethodField()
    review = serializers.SerializerMethodField()
    working_days = serializers.SerializerMethodField()

    class Meta:
        model = TakeOut
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
        return ItHas.objects.filter(takeouthas__take_out=obj).values('name')

    def get_files(self, obj):
        file = File.objects.filter(takeoutmedia__take_out=obj, is_main=True).first()
        if file is not None:
            return FileSerializer(file, context=self.context).data
        return None

    def get_working_days(self, obj):
        return

    def get_is_favorite(self, obj):  # TODO FIX
        return False

    def get_review(self, obj):  # TODO FIX
        return 5


class TakeOutDetailSerializer(serializers.ModelSerializer):
    food_types = serializers.SerializerMethodField()
    service_options = serializers.SerializerMethodField()
    it_has = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()
    working_days = serializers.SerializerMethodField()
    order_sites = serializers.SerializerMethodField()

    class Meta:
        model = TakeOut
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
        ]

    def get_food_types(self, obj):
        return FoodType.objects.filter(takeoutfoodtype__take_out=obj).values('id', 'name')

    def get_service_options(self, obj):
        return ServiceOption.objects.filter(takeoutserviceoption__take_out=obj).values('id', 'name')

    def get_it_has(self, obj):
        return ItHas.objects.filter(takeouthas__take_out=obj).values('name')

    def get_working_days(self, obj):
        return WorkingHours.objects.filter(takeoutworkingdays__take_out=obj).values(
            'id',
            'start_time',
            'end_time',
            'week_day',
            'is_holiday'
        )

    def get_files(self, obj):
        files = File.objects.filter(takeoutmedia__take_out=obj).order_by('ordering')
        if not files:
            return FileSerializer(files, many=True, context=self.context).data
        return None

    def get_order_sites(self, obj):
        return OrderSiteLink.objects.filter(takeoutordersite__take_out=obj).values('id', 'name')
