# model
from user.models import User
# rest
from rest_framework.response import Response
from rest_framework import status
# service
from user.services.email_verify import send_verify_code


def resend_verify_code(email):
    try:
        user = User.objects.get(email=email)
        send_verify_code(user)
        return Response({'detail': 'successfully send new code'})
    except User.DoesNotExist:
        return Response({'detail': 'email does not exist'}, status=status.HTTP_400_BAD_REQUEST)
