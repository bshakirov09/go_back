# Rest-Framework
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Project
from food_dining.models import (
    Restaurant,
    RestaurantHas,
    RestaurantFor,
    RestaurantFoodType,
    RestaurantServiceOption,
    RestaurantMedia,
    RestaurantOrderSite,
    RestaurantReserveSite
)


def update_restaurant(pk: int, **kwargs):
    restaurant: Restaurant = get_object_or_404(Restaurant, pk=pk)
    for key, value in kwargs.items():
        setattr(restaurant, key, value)
    restaurant.save()
    return Response({'detail': 'successfully updated'})


def update_restaurant_has(pk: int, it_has: list):
    restaurant: Restaurant = get_object_or_404(Restaurant, pk=pk)
    RestaurantHas.objects.filter(restaurant=restaurant).delete()

    for has in it_has:
        RestaurantHas.objects.create(restaurant=restaurant, it_has=has)
    return Response({'detail': 'successfully updated'})


def update_restaurant_good_for(pk: int, good_for: list):
    restaurant: Restaurant = get_object_or_404(Restaurant, pk=pk)
    RestaurantFor.objects.filter(restaurant=restaurant).delete()

    for good in good_for:
        RestaurantFor.objects.create(restaurant=restaurant, good_for=good)
    return Response({'detail': 'successfully updated'})


def update_restaurant_food_type(pk: int, food_type: list):
    restaurant: Restaurant = get_object_or_404(Restaurant, pk=pk)
    RestaurantFoodType.objects.filter(restaurant=restaurant).delete()

    for _type in food_type:
        RestaurantFoodType.objects.create(restaurant=restaurant, food_type=_type)
    return Response({'detail': 'successfully updated'})


def update_restaurant_service_option(pk: int, service_option: list):
    restaurant: Restaurant = get_object_or_404(Restaurant, pk=pk)
    RestaurantServiceOption.objects.filter(restaurant=restaurant).delete()

    for option in service_option:
        RestaurantServiceOption.objects.create(restaurant=restaurant, service_option=option)
    return Response({'detail': 'successfully updated'})


def update_restaurant_media(pk: int, files: list):
    restaurant: Restaurant = get_object_or_404(Restaurant, pk=pk)
    RestaurantMedia.objects.filter(restaurant=restaurant).delete()

    for file in files:
        RestaurantMedia.objects.create(restaurant=restaurant, file=file)
    return Response({'detail': 'successfully updated'})


def update_restaurant_order_sites(pk: int, order_sites: list):
    restaurant: Restaurant = get_object_or_404(Restaurant, pk=pk)
    RestaurantOrderSite.objects.filter(restaurant=restaurant).delete()

    for link in order_sites:
        RestaurantOrderSite.objects.create(restaurant=restaurant, link=link)
    return Response({'detail': 'successfully updated'})


def update_restaurant_reserve_sites(pk: int, reserve_sites: list):
    restaurant: Restaurant = get_object_or_404(Restaurant, pk=pk)
    RestaurantReserveSite.objects.filter(restaurant=restaurant).delete()

    for link in reserve_sites:
        RestaurantReserveSite.objects.create(restaurant=restaurant, link=link)
    return Response({'detail': 'successfully updated'})
