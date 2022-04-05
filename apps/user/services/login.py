# rest
from rest_framework.response import Response
from rest_framework import status
# django auth
from django.contrib.auth import authenticate
# model
from user.models import User
from rest_framework.authtoken.models import Token
# service
from user.services.signup import create_user
# lib
import requests
import facebook


def login(email: str, password):
    pleas_activate_your_email = 'please_activate_your_email'
    invalid_email_or_password = 'invalid_email_or_password'

    try:
        user = User.objects.get(email=email)
        if user.is_active is False:
            return Response({'detail': pleas_activate_your_email}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=user.username, password=password)
        if user is None:
            return Response({'detail': invalid_email_or_password}, status=status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    except User.DoesNotExist:
        return Response({'detail': invalid_email_or_password}, status=status.HTTP_400_BAD_REQUEST)


def login_with_google(access_token: str):
    google_url = "https://www.googleapis.com/oauth2/v3/userinfo"
    result = requests.get(f"{google_url}?access_token={access_token}")

    if result.status_code == 401:
        return Response({'detail': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)
    result = result.json()
    email = result['email']
    first_name = result['given_name']
    last_name = result['family_name']

    check_username = User.objects.filter(email__iexact=email).exclude(social_network=User.GOOGLE).exists()
    if check_username is True:
        return Response({'detail': 'username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email__iexact=email, social_network=User.GOOGLE)
    except User.DoesNotExist:
        user = create_user(first_name, last_name, email, User.GOOGLE)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


def login_with_facebook(access_token: str):
    try:
        graph = facebook.GraphAPI(access_token=access_token)
        profile = graph.request("/me?fields=name")
        email = f'{profile["name"]}@gmail.com'

        check_username = User.objects.filter(email__iexact=email).exclude(social_network=User.FACEBOOK).exists()
        if check_username is True:
            return Response({'detail': 'username already exists'}, status=400)

        try:
            user = User.objects.get(email__iexact=email, social_network=User.FACEBOOK)
        except User.DoesNotExist:
            user = create_user('', '', email, User.FACEBOOK)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

    except facebook.GraphAPIError:
        return Response({'detail': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)
