# rest
from rest_framework.response import Response
from rest_framework import status
# model
from user.models import User
# service
from user.services.email_verify import send_verify_code


def signup_with_local(first_name: str, last_name: str, email: str, password):
    check_email = User.objects.filter(email__iexact=email).exists()
    if check_email is True:
        return Response({'detail': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)
    user = create_user(first_name, last_name, email, User.LOCAL, password=password)
    send_verify_code(user)
    return Response({'detail': 'successfully registered'}, status=status.HTTP_201_CREATED)


def create_user(
        first_name: str,
        last_name: str,
        email: str,
        social_network: str,
        password=None
):
    user = User.objects.create(
        username=email,
        email=email,
        first_name=first_name,
        last_name=last_name,
        is_active=False if social_network == User.LOCAL else True,
        is_staff=False,
        is_superuser=False,
        social_network=social_network
    )
    if password:
        user.set_password(password)
        user.save()

    return user
