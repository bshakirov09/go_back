from file.models import File
from food_dining.models.base_model import *
from django.db import models


class Bakery(BaseFoodDiningModel):
    type_model = models.CharField(max_length=48, choices=KosherType.choices)


class BakeryWorkingDays(BaseModel):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE)
    working_hour = models.ForeignKey(WorkingHours, on_delete=models.CASCADE)


class BakeryHas(BaseModel):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE)
    it_has = models.ForeignKey(ItHas, on_delete=models.CASCADE)


class BakeryOrderSite(BaseModel):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE)
    link = models.ForeignKey(OrderSiteLink, on_delete=models.CASCADE, null=True)


class BakeryFoodType(BaseModel):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)


class BakeryServiceOption(BaseModel):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE)
    service_option = models.ForeignKey(ServiceOption, on_delete=models.CASCADE)


class BakeryMenu(BaseModel):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class BakeryMeal(BaseModel):
    menu = models.ForeignKey(BakeryMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ForeignKey(File, on_delete=models.PROTECT)


class BakeryMedia(BaseModel):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
