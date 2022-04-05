# rest
from rest_framework.response import Response
from rest_framework import status
# model
from user.models import User
# service
from user.services.email_verify import send_verify_code, check_verify_forgot_password_code, VerifyEmail


def send_forgot_password_code(email: str):
    try:
        user = User.objects.get(email=email)
        send_verify_code(user, is_forgot_password=True)
        return Response({'detail': 'successfully'})
    except User.DoesNotExist:
        return Response({'detail': 'email does not exists'}, status=status.HTTP_400_BAD_REQUEST)


def check_forgot_password_code(email: str, code: str):
    return Response({'status': check_verify_forgot_password_code(email, code)})


def set_new_password(email: str, code: str, new_password: str):
    try:
        check_code = check_verify_forgot_password_code(email, code)
        if check_code is False:
            return Response({'detail': 'invalid code'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(email=email)
        user.set_password(new_password)
        user.save()
        VerifyEmail.objects.filter(
            user__email=email,
            code=f'forgot_password_{code}',
            is_active=False
        ).update(is_active=True)
        return Response({'detail': 'successfully'})
    except User.DoesNotExist:
        return Response({'detail': 'email does not exists'}, status=status.HTTP_400_BAD_REQUEST)
