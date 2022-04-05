# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from file.models import File
from user.models import User


def user_update(user: User, **kwargs):
    email = kwargs.get('email')
    kwargs['username'] = email
    check_email = User.objects.filter(email__iexact=email).exists()
    if user.email != email and check_email:
        return Response({'detail': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)
    for key, value in kwargs.items():
        setattr(user, key, value)
    user.save()
    return Response(
        data={'status': 'Successful updated'},
        status=status.HTTP_200_OK
    )


def user_avatar_update(user: User, avatar: File):
    user.avatar = avatar
    user.save()
    return Response(
        data={'status': 'Successful updated'},
        status=status.HTTP_200_OK
    )
