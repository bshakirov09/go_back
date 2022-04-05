# Rest-Framework
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Project
from food_dining.models import (
    FoodService
)


def update_food_service(pk: int, **kwargs):
    food_service: FoodService = get_object_or_404(FoodService, pk=pk)
    for key, value in kwargs.items():
        setattr(food_service, key, value)
    food_service.save()
    return Response({'detail': 'successfully updated'})
