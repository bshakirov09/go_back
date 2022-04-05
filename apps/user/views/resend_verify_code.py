# rest
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
# serializer
from user.serializers.resend_verify_code import ResendVerifyCodeSerializer
# service
from user.services.resend_verify_code import resend_verify_code


class ResendVerifyCodeView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serialize = ResendVerifyCodeSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        return resend_verify_code(**serialize.validated_data)
