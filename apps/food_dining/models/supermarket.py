from file.models import File
from food_dining.models.base_model import *
from django.db import models


class SuperMarket(BaseFoodDiningModel):
    type_model = models.CharField(max_length=48, choices=KosherType.choices)


class SuperMarketWorkingDays(BaseModel):
    supermarket = models.ForeignKey(SuperMarket, on_delete=models.CASCADE)
    working_hour = models.ForeignKey(WorkingHours, on_delete=models.CASCADE)


class SuperMarketHas(BaseModel):
    supermarket = models.ForeignKey(SuperMarket, on_delete=models.CASCADE)
    it_has = models.ForeignKey(ItHas, on_delete=models.CASCADE)


class SuperMarketOrderSite(BaseModel):
    supermarket = models.ForeignKey(SuperMarket, on_delete=models.CASCADE)
    link = models.ForeignKey(OrderSiteLink, on_delete=models.CASCADE, null=True)


class SuperMarketFoodType(BaseModel):
    supermarket = models.ForeignKey(SuperMarket, on_delete=models.CASCADE)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)


class SuperMarketServiceOption(BaseModel):
    supermarket = models.ForeignKey(SuperMarket, on_delete=models.CASCADE)
    service_option = models.ForeignKey(ServiceOption, on_delete=models.CASCADE)


class SuperMarketMenu(BaseModel):
    supermarket = models.ForeignKey(SuperMarket, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class SuperMarketMeal(BaseModel):
    menu = models.ForeignKey(SuperMarketMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ForeignKey(File, on_delete=models.PROTECT)


class SuperMarketMedia(BaseModel):
    supermarket = models.ForeignKey(SuperMarket, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
