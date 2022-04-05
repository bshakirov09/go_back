# Rest-Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Project
from user.serializers.me import UserMeSerializer


class UserMeAPIVIew(APIView):
    serializers_class = UserMeSerializer

    def get(self, request):
        context = {'request': request}
        serializer = self.serializers_class(request.user, context=context)
        return Response(data=serializer.data)
