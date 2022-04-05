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
    FoodType,
    ServiceOption
)
from food_dining.models import (
    TakeOut,
    TakeOutWorkingDays,
    TakeOutHas,
    TakeOutOrderSite,
    TakeOutFoodType,
    TakeOutServiceOption,
    TakeOutMedia
)

# Service
from food_dining.services.work_days import create_default_working_days


def create_take_out(
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
        food_type: typing.List[FoodType],
        service_option: typing.List[ServiceOption],
        files: typing.List[File],
        order_sites: typing.List,
):
    take_out = TakeOut.objects.create(
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
        TakeOutHas.objects.create(
            take_out=take_out,
            it_has=has
        )

    for food in food_type:
        TakeOutFoodType.objects.create(
            take_out=take_out,
            food_type=food
        )

    for option in service_option:
        TakeOutServiceOption.objects.create(
            take_out=take_out,
            service_option=option
        )

    for file in files:
        TakeOutMedia.objects.create(
            take_out=take_out,
            file=file
        )

    for order_site in order_sites:
        TakeOutOrderSite.objects.create(
            take_out=take_out,
            link=order_site
        )
    create_default_working_days(TakeOutWorkingDays, take_out, 'take_out')
    return Response(
        data={'detail': 'successful created'},
        status=status.HTTP_201_CREATED
    )
