from file.models import File
from food_dining.models.base_model import *
from core.base_model import BaseModel
from django.db import models


class FoodService(BaseFoodDiningModel):
    type_model = models.CharField(max_length=25, choices=TypeModel.choices)


class FoodServiceWorkingDays(BaseModel):
    food_service = models.ForeignKey(FoodService, on_delete=models.CASCADE)
    working_hour = models.ForeignKey(WorkingHours, on_delete=models.CASCADE)


class FoodServiceHas(BaseModel):
    food_service = models.ForeignKey(FoodService, on_delete=models.CASCADE)
    it_has = models.ForeignKey(ItHas, on_delete=models.CASCADE)


class FoodServiceFor(BaseModel):
    food_service = models.ForeignKey(FoodService, on_delete=models.CASCADE)
    good_for = models.ForeignKey(GoodFor, on_delete=models.CASCADE)


class FoodServiceOrderSite(BaseModel):
    food_service = models.ForeignKey(FoodService, on_delete=models.CASCADE)
    link = models.ForeignKey(OrderSiteLink, on_delete=models.CASCADE, null=True)


class FoodServiceReserveSite(BaseModel):
    food_service = models.ForeignKey(FoodService, on_delete=models.CASCADE)
    link = models.ForeignKey(ReserveSiteLink, on_delete=models.CASCADE, null=True)


class FoodServiceFoodType(BaseModel):
    food_service = models.ForeignKey(FoodService, on_delete=models.CASCADE)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)


class FoodServiceOption(BaseModel):
    food_service = models.ForeignKey(FoodService, on_delete=models.CASCADE)
    service_option = models.ForeignKey(ServiceOption, on_delete=models.CASCADE)


class FoodServiceMenu(BaseModel):
    food_service = models.ForeignKey(FoodService, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class FoodServiceMeal(BaseModel):
    menu = models.ForeignKey(FoodServiceMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ForeignKey(File, on_delete=models.PROTECT)


class FoodServiceMedia(BaseModel):
    food_service = models.ForeignKey(FoodService, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
