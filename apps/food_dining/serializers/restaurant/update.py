# Rest-Framework
from rest_framework import serializers

# Models
from food_dining.models.base_model import TypeModel
from food_dining.serializers.base import BaseFoodDiningSerializer


class RestaurantUpdateSerializer(BaseFoodDiningSerializer):
    """
    name: str
    phone_number: str
    website: str
    latitude: str
    longitude: str
    please_note: str
    twitter_url: str
    instagram_url: str
    facebook_url: str
    country: srt
    city: str
    """
    type_model = serializers.ChoiceField(choices=TypeModel.choices)
