#Django
from django.db import models
#Project
from core.base_model import BaseModel
from core.Singelton.singelton import SingeltonModel


class PrivacyPolicy(SingeltonModel, BaseModel):
    description = models.TextField()