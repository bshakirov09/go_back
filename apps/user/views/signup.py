# rest
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
# serializer
from user.serializers.signup import SignupSerializer
# services
from user.services.signup import signup_with_local


class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return signup_with_local(**serializer.validated_data)
