from file.models import File
from food_dining.models.base_model import *
from core.base_model import BaseModel
from django.db import models


class TakeOut(BaseFoodDiningModel):
    type_model = models.CharField(max_length=25, choices=TypeModel.choices)


class TakeOutWorkingDays(BaseModel):
    take_out = models.ForeignKey(TakeOut, on_delete=models.CASCADE)
    working_hour = models.ForeignKey(WorkingHours, on_delete=models.CASCADE)


class TakeOutHas(BaseModel):
    take_out = models.ForeignKey(TakeOut, on_delete=models.CASCADE)
    it_has = models.ForeignKey(ItHas, on_delete=models.CASCADE)


class TakeOutOrderSite(BaseModel):
    take_out = models.ForeignKey(TakeOut, on_delete=models.CASCADE)
    link = models.ForeignKey(OrderSiteLink, on_delete=models.CASCADE, null=True)


class TakeOutFoodType(BaseModel):
    take_out = models.ForeignKey(TakeOut, on_delete=models.CASCADE)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)


class TakeOutServiceOption(BaseModel):
    take_out = models.ForeignKey(TakeOut, on_delete=models.CASCADE)
    service_option = models.ForeignKey(ServiceOption, on_delete=models.CASCADE)


class TakeOutMenu(BaseModel):
    take_out = models.ForeignKey(TakeOut, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class TakeOutMeal(BaseModel):
    menu = models.ForeignKey(TakeOutMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ForeignKey(File, on_delete=models.PROTECT)


class TakeOutMedia(BaseModel):
    take_out = models.ForeignKey(TakeOut, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
