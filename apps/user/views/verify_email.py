# rest
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
# serializer
from user.serializers.verify_email import VerifyEmailSerializer
# service
from user.services.email_verify import check_verify_signup_code


class EmailVerifyView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = VerifyEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return check_verify_signup_code(**serializer.validated_data)
