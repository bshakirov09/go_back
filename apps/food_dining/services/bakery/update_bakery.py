from rest_framework.generics import get_object_or_404

from food_dining.models.bakery import *
from rest_framework.response import Response
import typing


def update_bakery(
        pk: int,
        name: str,
        phone_number: str,
        website: str,
        latitude: str,
        longitude: str,
        please_note: str,
        twitter_url: str,
        facebook_url: str,
        instagram_url: str,
        country: str,
        city: str,
        type_model: str
) -> Response:
    """
    :param pk:
    :param name:
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
    :return: Response
    """
    instance: Bakery = get_object_or_404(Bakery, pk=pk)
    instance.name = name
    instance.phone_number = phone_number
    instance.website = website
    instance.latitude = latitude
    instance.longitude = longitude
    instance.please_note = please_note
    instance.twitter_url = twitter_url
    instance.facebook_url = facebook_url
    instance.instagram_url = instagram_url
    instance.country = country
    instance.city = city
    instance.type_model = type_model
    instance.save()
    return Response({'detail': 'successfully updated'})


def update_has(pk: int, it_has: typing.List[ItHas]) -> Response:
    """
    :param pk: int
    :param it_has: list
    :return: Response
    """
    instance: Bakery = get_object_or_404(Bakery, pk=pk)
    BakeryHas.objects.filter(bakery=instance).delete()

    for has in it_has:
        BakeryHas.objects.create(bakery=instance, it_has=has)
    return Response({'detail': 'successfully updated'})


def update_food_type(pk: int, food_type: typing.List[FoodType]) -> Response:
    """
    :param pk:
    :param food_type:
    :return: Response
    """
    instance: Bakery = get_object_or_404(Bakery, pk=pk)
    BakeryFoodType.objects.filter(bakery=instance).delete()

    for food in food_type:
        BakeryFoodType.objects.create(bakery=instance, food_type=food)
    return Response({'detail': 'successfully updated'})


def update_service_option(pk: int, service_option: typing.List[ServiceOption]) -> Response:
    """
    :param pk:
    :param service_option:
    :return: Response
    """
    instance: Bakery = get_object_or_404(Bakery, pk=pk)
    BakeryServiceOption.objects.filter(bakery=instance).delete()

    for service in service_option:
        BakeryServiceOption.objects.create(bakery=instance, service_option=service)
    return Response({'detail': 'successfully updated'})


def update_order_site(pk: int, order_sites: typing.List[typing.Dict[str, str]]) -> Response:
    """
    :param pk:
    :param urls:
    :return: Response
    """
    instance: Bakery = get_object_or_404(Bakery, pk=pk)
    BakeryOrderSite.objects.filter(bakery=instance).delete()
    for url in order_sites:
        BakeryOrderSite.objects.create(bakery=instance, link=url)
    return Response({'detail': 'successfully updated'})


def update_media(pk: int, files: typing.List[File]) -> Response:
    """

    :param pk:
    :return: Response
    """
    instance: Bakery = get_object_or_404(Bakery, pk=pk)
    BakeryMedia.objects.filter(bakery=instance).delete()
    for file in files:
        BakeryMedia.objects.create(bakery=instance, file=file)
    return Response({'detail': 'successfully updated'})


__all__ = [
    'update_media',
    'update_food_type',
    'update_has',
    'update_service_option',
    'update_order_site',
    'update_bakery'
]
