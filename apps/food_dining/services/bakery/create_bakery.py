from food_dining.models.bakery import *
import typing
from rest_framework.response import Response
from rest_framework import status

from food_dining.services.work_days import create_default_working_days


def create_bakery(
        name: str,
        food_type: typing.List[FoodType],
        service_option: typing.List[ServiceOption],
        it_has: typing.List[ItHas],
        files: typing.List[File],
        order_sites: typing.List[OrderSiteLink],
        type_model: str,
        phone_number: str,
        website: str,
        latitude: str,
        longitude: str,
        please_note: str,
        twitter_url: typing.Optional[str],
        facebook_url: typing.Optional[str],
        instagram_url: typing.Optional[str],
        country: str,
        city: str,
        creator: User
) -> Response:
    """
    :param name:
    :param food_type:
    :param service_option:
    :param it_has:
    :param files:
    :param order_sites:
    :param type_model:
    :param phone_number:
    :param website:
    :param latitude:
    :param longitude:
    :param please_note:
    :param twitter_url:
    :param facebook_url:
    :param instagram_url:
    :param country:
    :param city:
    :param creator:
    :return:
    """
    bakery = Bakery.objects.create(
        type_model=type_model,
        name=name,
        phone_number=phone_number,
        website=website,
        latitude=latitude,
        longitude=longitude,
        please_note=please_note,
        twitter_url=twitter_url,
        instagram_url=instagram_url,
        facebook_url=facebook_url,
        country=country,
        city=city,
        creator=creator
    )

    for food in food_type:
        BakeryFoodType.objects.create(
            bakery=bakery,
            food_type=food
        )

    for service in service_option:
        BakeryServiceOption.objects.create(
            bakery=bakery,
            service_option=service
        )

    for has in it_has:
        BakeryHas.objects.create(
            bakery=bakery,
            it_has=has
        )
    for file in files:
        BakeryMedia.objects.create(
            bakery=bakery,
            file=file
        )

    for link in order_sites:
        BakeryOrderSite.objects.create(
            bakery=bakery,
            link=link
        )

    create_default_working_days(BakeryWorkingDays, bakery, 'bakery')

    return Response({"detail": 'successfully'}, status=status.HTTP_201_CREATED)
