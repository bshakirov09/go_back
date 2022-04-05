# Rest-Framework
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Project
from food_dining.models import (
    TakeOut,
    TakeOutHas,
    TakeOutOrderSite,
    TakeOutFoodType,
    TakeOutServiceOption,
    TakeOutMedia
)


def update_take_out(pk: int, **kwargs):
    take_out: TakeOut = get_object_or_404(TakeOut, pk=pk)
    for key, value in kwargs.items():
        setattr(take_out, key, value)
    take_out.save()
    return Response({'detail': 'successfully updated'})


def update_takeout_has(pk: int, it_has: list):
    take_out: TakeOut = get_object_or_404(TakeOut, pk=pk)
    TakeOutHas.objects.filter(take_out=take_out).delete()

    for has in it_has:
        TakeOutHas.objects.create(take_out=take_out, it_has=has)
    return Response({'detail': 'successfully updated'})


def update_takeout_food_type(pk: int, food_type: list):
    take_out: TakeOut = get_object_or_404(TakeOut, pk=pk)
    TakeOutFoodType.objects.filter(take_out=take_out).delete()

    for _type in food_type:
        TakeOutFoodType.objects.create(take_out=take_out, food_type=_type)
    return Response({'detail': 'successfully updated'})


def update_takeout_service_option(pk: int, service_option: list):
    take_out: TakeOut = get_object_or_404(TakeOut, pk=pk)
    TakeOutServiceOption.objects.filter(take_out=take_out).delete()

    for option in service_option:
        TakeOutServiceOption.objects.create(take_out=take_out, service_option=option)
    return Response({'detail': 'successfully updated'})


def update_takeout_media(pk: int, files: list):
    take_out: TakeOut = get_object_or_404(TakeOut, pk=pk)
    TakeOutMedia.objects.filter(take_out=take_out).delete()

    for file in files:
        TakeOutMedia.objects.create(take_out=take_out, file=file)
    return Response({'detail': 'successfully updated'})


def update_takeout_order_sites(pk: int, order_sites: list):
    take_out: TakeOut = get_object_or_404(TakeOut, pk=pk)
    TakeOutOrderSite.objects.filter(take_out=take_out).delete()

    for link in order_sites:
        TakeOutOrderSite.objects.create(take_out=take_out, link=link)
    return Response({'detail': 'successfully updated'})
