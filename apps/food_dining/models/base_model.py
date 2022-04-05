from core.base_model import BaseModel
from django.db import models
from user.models import User


class FoodType(BaseModel):
    name = models.CharField(max_length=255)


class ServiceOption(BaseModel):
    name = models.CharField(max_length=255)


class OrderSiteLink(BaseModel):
    name = models.TextField(max_length=555)


class ReserveSiteLink(BaseModel):
    name = models.CharField(max_length=555)


class ItHas(BaseModel):
    name = models.CharField(max_length=255)


class GoodFor(BaseModel):
    name = models.CharField(max_length=255)


class WorkingHours(BaseModel):
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'

    WEEK_DAYS = (
        (MONDAY, MONDAY),
        (TUESDAY, TUESDAY),
        (WEDNESDAY, WEDNESDAY),
        (THURSDAY, THURSDAY),
        (FRIDAY, FRIDAY),
        (SATURDAY, SATURDAY),
        (SUNDAY, SUNDAY)
    )

    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    week_day = models.CharField(max_length=25, choices=WEEK_DAYS)
    is_holiday = models.BooleanField(default=False)


class TypeModel:
    DAIRY = 'dairy'
    PAREVE = 'pareve'
    MEAT = 'meat'
    choices = ((DAIRY, DAIRY), (PAREVE, PAREVE), (MEAT, MEAT))


class KosherType:
    KOSHER_GROCERY = 'kosher_grocery'
    SOME_KOSHER_ITEMS = 'some_kosher_items'
    KOSHER_BAKERY = 'kosher_bakery'
    choices = ((KOSHER_GROCERY, KOSHER_GROCERY), (SOME_KOSHER_ITEMS, SOME_KOSHER_ITEMS), (KOSHER_BAKERY, KOSHER_BAKERY))


class BaseFoodDiningModel(BaseModel):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=35)
    website = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    please_note = models.TextField()
    twitter_url = models.CharField(max_length=355, null=True)
    instagram_url = models.CharField(max_length=355, null=True)
    facebook_url = models.CharField(max_length=355, null=True)
    country = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True
