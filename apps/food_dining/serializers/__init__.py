from rest_framework import serializers
from food_dining.models.base_model import WorkingHours


class WorkingDaysSerializer(serializers.Serializer):
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    week_day = serializers.ChoiceField(WorkingHours.WEEK_DAYS)
    is_holiday = serializers.BooleanField(default=False)


class OrderSitesSerializer(serializers.Serializer):
    url = serializers.CharField()
