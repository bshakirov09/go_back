# Django
from django.db import models
# Project
from core.base_model import BaseModel
from file.models import File


class Tag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Explore(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=10, decimal_places=10)
    longitude = models.DecimalField(max_digits=10, decimal_places=10)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ExploreImage(BaseModel):
    explore = models.ForeignKey(Explore, on_delete=models.CASCADE, related_name='explore')
    file = models.ForeignKey(File, on_delete=models.PROTECT)


class ExploreTag(BaseModel):
    explore = models.ForeignKey(Explore, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
