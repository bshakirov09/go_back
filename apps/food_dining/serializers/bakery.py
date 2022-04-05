from rest_framework import serializers
from food_dining.models.base_model import FoodType, ServiceOption, ItHas, KosherType, OrderSiteLink
from food_dining.models.bakery import BakeryMenu, BakeryMeal, Bakery, WorkingHours
from file.serializers import FileSerializer, File
from food_dining.serializers.base import BaseFoodDiningSerializer


class BakeryCreateSerializer(BaseFoodDiningSerializer):
    food_type = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=FoodType.objects.all())
    )
    service_option = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=ServiceOption.objects.all())
    )
    it_has = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=ItHas.objects.all())
    )
    files = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=File.objects.all())
    )
    order_sites = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=OrderSiteLink.objects.all())
    )
    type_model = serializers.ChoiceField(KosherType.choices)


class BakeryUpdateSerializer(BaseFoodDiningSerializer):
    type_model = serializers.ChoiceField(choices=KosherType.choices)


class BakeryMenuModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryMenu
        fields = ['id', 'name', 'bakery']


class BakeryMealModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryMeal
        fields = ['id', 'menu', 'name', 'price', 'description', 'photo']

    def to_representation(self, instance):
        self.fields['photo'] = FileSerializer(context=self.context)
        self.fields['menu'] = BakeryMenuModelSerializer()
        return super(BakeryMealModelSerializer, self).to_representation(instance)


class BakeryDetailSerializer(serializers.ModelSerializer):
    food_types = serializers.SerializerMethodField()
    service_options = serializers.SerializerMethodField()
    it_has = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()
    working_days = serializers.SerializerMethodField()
    order_sites = serializers.SerializerMethodField()

    class Meta:
        model = Bakery
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
            'order_sites'
        ]

    def get_food_types(self, obj):
        return FoodType.objects.filter(bakeryfoodtype__bakery=obj).values('id', 'name')

    def get_service_options(self, obj):
        return ServiceOption.objects.filter(bakeryserviceoption__bakery=obj).values('id', 'name')

    def get_it_has(self, obj):
        return ItHas.objects.filter(bakeryhas__bakery=obj).values('id', 'name')

    def get_order_sites(self, obj):
        return OrderSiteLink.objects.filter(bakeryordersite__bakery=obj).values('id', 'name')

    def get_working_days(self, obj):
        return WorkingHours.objects.filter(bakeryworkingdays__bakery=obj).values(
            'id',
            'start_time',
            'end_time',
            'week_day',
            'is_holiday'
        )

    def get_files(self, obj):
        files = File.objects.filter(bakerymedia__bakery=obj).order_by('ordering')
        if not files:
            return FileSerializer(files, many=True, context=self.context).data
        return None


class BakeryListSerializer(serializers.ModelSerializer):
    it_has = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()
    is_favorite = serializers.SerializerMethodField()
    review = serializers.SerializerMethodField()
    working_days = serializers.SerializerMethodField()

    class Meta:
        model = Bakery
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
        return ItHas.objects.filter(bakeryhas__bakery=obj).values('name')

    def get_files(self, obj):
        file = File.objects.filter(bakerymedia__bakery=obj, is_main=True).first()
        if file is not None:
            return FileSerializer(file, context=self.context).data
        return None

    def get_working_days(self, obj):
        return

    def get_is_favorite(self, obj):  # TODO FIX
        return False

    def get_review(self, obj):  # TODO FIX
        return 5


__all__ = [
    'BakeryCreateSerializer',
    'BakeryUpdateSerializer',
    'BakeryMenuModelSerializer',
    'BakeryMealModelSerializer',
    'BakeryListSerializer',
    'BakeryDetailSerializer'
]
