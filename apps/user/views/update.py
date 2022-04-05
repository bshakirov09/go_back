# Rest-Framework
from rest_framework.views import APIView

# Project
from user.serializers.update import UserUpdateSerializer, UserAvatarUpdateSerializer
from user.services.update import user_update, user_avatar_update


class UserUpdateAPIView(APIView):
    serializer_class = UserUpdateSerializer

    def put(self, request):
        user = request.user
        serializer = self.serializer_class(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        return user_update(user=user, **serializer.validated_data)


class UserAvatarUpdate(APIView):
    serializer_class = UserAvatarUpdateSerializer

    def put(self, request):
        user = request.user
        serializer = self.serializer_class(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        return user_avatar_update(user=user, avatar=serializer.validated_data['avatar'])
