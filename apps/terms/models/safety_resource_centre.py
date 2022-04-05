#Django
from django.db import models
#Project
from core.base_model import BaseModel
from core.Singelton.singelton import SingeltonModel


class SafetyResourceCentre(SingeltonModel, BaseModel):
    description = models.TextField()