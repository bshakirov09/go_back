# Python
import typing
from decimal import Decimal

# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Models
from file.models import File
from food_dining.models.base_model import (
    ItHas,
    GoodFor,
    FoodType,
    ServiceOption
)
from food_dining.models import (
    Restaurant,
    RestaurantHas,
    RestaurantFor,
    RestaurantOrderSite,
    RestaurantReserveSite,
    RestaurantFoodType,
    RestaurantServiceOption,
    RestaurantMedia,
    RestaurantWorkingDays
)

# Service
from food_dining.services.work_days import create_default_working_days


def create_restaurant(
        name: str,
        phone_number: str,
        type_model: str,
        website: str,
        latitude: Decimal,
        longitude: Decimal,
        please_note: str,
        twitter_url: typing.Optional[str],
        facebook_url: typing.Optional[str],
        instagram_url: typing.Optional[str],
        country: str,
        city: str,
        it_has: typing.List[ItHas],
        good_for: typing.List[GoodFor],
        food_type: typing.List[FoodType],
        service_option: typing.List[ServiceOption],
        files: typing.List[File],
        order_sites: typing.List,
        reserve_sites: typing.List
):
    restaurant = Restaurant.objects.create(
        name=name,
        phone_number=phone_number,
        type_model=type_model,
        website=website,
        latitude=latitude,
        longitude=longitude,
        please_note=please_note,
        twitter_url=twitter_url,
        facebook_url=facebook_url,
        instagram_url=instagram_url,
        country=country,
        city=city
    )

    for has in it_has:
        RestaurantHas.objects.create(
            restaurant=restaurant,
            it_has=has
        )

    for good in good_for:
        RestaurantFor.objects.create(
            restaurant=restaurant,
            good_for=good
        )

    for food in food_type:
        RestaurantFoodType.objects.create(
            restaurant=restaurant,
            food_type=food
        )

    for option in service_option:
        RestaurantServiceOption.objects.create(
            restaurant=restaurant,
            service_option=option
        )

    for file in files:
        RestaurantMedia.objects.create(
            restaurant=restaurant,
            file=file
        )

    for order_site in order_sites:
        RestaurantOrderSite.objects.create(
            restaurant=restaurant,
            link=order_site
        )

    for reserve_site in reserve_sites:
        RestaurantReserveSite.objects.create(
            restaurant=restaurant,
            link=reserve_site
        )
    create_default_working_days(RestaurantWorkingDays, restaurant, 'restaurant')
    return Response(
        data={'detail': 'successful created'},
        status=status.HTTP_201_CREATED
    )
