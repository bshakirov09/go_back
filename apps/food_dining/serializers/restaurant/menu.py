# Rest-Framework
from rest_framework import serializers

# Project
from food_dining.models import RestaurantMenu, RestaurantMeal
from file.serializers import FileSerializer


class RestaurantMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantMenu
        fields = [
            'id',
            'name',
            'restaurant'
        ]


class RestaurantMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantMeal
        fields = [
            'id',
            'menu',
            'name',
            'price',
            'description',
            'photo'
        ]

    def to_representation(self, instance):
        self.fields['menu'] = RestaurantMenuSerializer()
        self.fields['photo'] = FileSerializer(context=self.context)
        return super(RestaurantMealSerializer, self).to_representation(instance)
