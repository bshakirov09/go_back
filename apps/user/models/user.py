# Django
from django.contrib.auth.models import AbstractUser
from django.db import models

# Project
from file.models import File


class User(AbstractUser):
    SIMPLE_USER = 'simple_user'
    VENDOR_USER = 'vendor_user'

    LOCAL = 'local'
    GOOGLE = 'google'
    FACEBOOK = 'facebook'
    APPLE = 'apple'

    OTHER = 'other'
    MALE = 'male'
    FEMALE = 'female'
    TYPE_USER = ((SIMPLE_USER, SIMPLE_USER), ((VENDOR_USER, VENDOR_USER)))
    GENDER = ((MALE, MALE), (FEMALE, FEMALE), (OTHER, OTHER))
    SOCIAL_NETWORK = ((LOCAL, LOCAL), (GOOGLE, GOOGLE), (FACEBOOK, FACEBOOK), (APPLE, APPLE))

    avatar = models.ForeignKey(File, models.PROTECT, related_name='avatars', null=True)
    user_type = models.CharField(max_length=35, choices=TYPE_USER, default=SIMPLE_USER)
    phone_number = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=35, default=OTHER, choices=GENDER)
    birthday = models.DateField(null=True)
    social_network = models.CharField(max_length=35, default=LOCAL)
    city = models.CharField(max_length=255, null=True)
