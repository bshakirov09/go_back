from user.models.user import User
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


def change_password(user: User, current_password: str, new_password: str) -> Response:
    if user.check_password(current_password) is False:
        return Response({'detail': 'invalid current password'}, status=HTTP_400_BAD_REQUEST)
    user.set_password(new_password)
    user.save()
    return Response({'detail': 'successfully saved'})
