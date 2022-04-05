from rest_framework.generics import GenericAPIView
from user.serializers.change_password import ChangePasswordSerializer
from rest_framework import permissions
from user.services.change_password import change_password


class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return change_password(user=request.user, **serializer.validated_data)
