# rest
from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny
# serializer
from user.serializers.login import LoginSerializer, LoginSocialNetworkSerializer
# service
from user.services.login import login, login_with_google, login_with_facebook


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return login(**serializer.validated_data)


class LoginSocialNetworkView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSocialNetworkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        type_token = serializer.validated_data['type_token']
        access_token = serializer.validated_data['access_token']

        if type_token == 'google':
            return login_with_google(access_token)
        elif type_token == 'facebook':
            return login_with_facebook(access_token)

        return Response({'detail': 'not found social network'}, status=400)
