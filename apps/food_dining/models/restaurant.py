# Dajngo
from django.db import models

# Models
from core.base_model import BaseModel
from file.models import File
from food_dining.models.base_model import (
    BaseFoodDiningModel,
    TypeModel,
    WorkingHours,
    ItHas,
    GoodFor,
    OrderSiteLink,
    ReserveSiteLink,
    FoodType,
    ServiceOption
)


class Restaurant(BaseFoodDiningModel):
    type_model = models.CharField(max_length=25, choices=TypeModel.choices)


class RestaurantWorkingDays(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    working_hour = models.ForeignKey(WorkingHours, on_delete=models.CASCADE)


class RestaurantHas(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    it_has = models.ForeignKey(ItHas, on_delete=models.CASCADE)


class RestaurantFor(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    good_for = models.ForeignKey(GoodFor, on_delete=models.CASCADE)


class RestaurantOrderSite(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    link = models.ForeignKey(OrderSiteLink, on_delete=models.CASCADE, null=True)


class RestaurantReserveSite(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    link = models.ForeignKey(ReserveSiteLink, on_delete=models.CASCADE, null=True)


class RestaurantFoodType(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)


class RestaurantServiceOption(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    service_option = models.ForeignKey(ServiceOption, on_delete=models.CASCADE)


class RestaurantMenu(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class RestaurantMeal(BaseModel):
    menu = models.ForeignKey(RestaurantMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ForeignKey(File, on_delete=models.PROTECT)


class RestaurantMedia(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
