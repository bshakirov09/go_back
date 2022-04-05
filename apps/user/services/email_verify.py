from user.models.verify_email import VerifyEmail
from random import randint
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from notification.services.send_email import send_email_with_send_grid

SIGNUP_EMAIL_TEMPLATE = """
Hello {email}

Are you ready to gain access to all of the assets we prepared for clients of GoPlaciz?

First, you must complete your registration by entering on the code below:

{code}

This code will verify your email address, and then you will officially be a part of the GoPlaciz community.

See you there!

Best regards, the GoPlaciz team"""


def send_verify_code(user, is_forgot_password=False):
    code = randint(100_000, 999_999)
    if is_forgot_password is False:
        VerifyEmail.objects.create(
            user=user,
            code=f'verify_email_{code}',
            is_active=False
        )
    elif is_forgot_password is True:
        VerifyEmail.objects.create(
            user=user,
            code=f'forgot_password_{code}',
            is_active=False
        )
    send_email_with_send_grid(
        user.email, 'Verification email',
        SIGNUP_EMAIL_TEMPLATE.format(code=code, email=user.email)
    )


def check_verify_signup_code(email, code):
    check = VerifyEmail.objects.filter(
        user__email=email,
        code=f'verify_email_{code}',
        is_active=False
    )
    if check.exists():
        verify = check.first()
        verify.is_active = True
        verify.save()
        user = verify.user
        user.is_active = True
        user.save()

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

    else:
        return Response({'detail': 'invalid code'}, status=status.HTTP_400_BAD_REQUEST)


def check_verify_forgot_password_code(email, code):
    check = VerifyEmail.objects.filter(
        user__email=email,
        code=f'forgot_password_{code}',
        is_active=False
    )
    return check.exists()
