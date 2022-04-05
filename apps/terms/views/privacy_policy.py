#Rest Framework
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
#Project
from terms.models.privacy_policy import PrivacyPolicy
from terms.serializers.privacy_policy import PrivacyPolicySerializer


class CreatePrivacyPolicyView(CreateAPIView):
    serializer_class = PrivacyPolicySerializer
    permission_classes = (AllowAny,)


class GetPrivacyPolicyView(APIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = PrivacyPolicySerializer

    def get(self, *args, **kwargs):
        queryset = PrivacyPolicy.objects.all().first()
        serializer = self.serializer_class(instance=queryset)
        return Response(serializer.data)