#Rest Framework
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
#Project
from terms.models.safety_resource_centre import SafetyResourceCentre
from terms.serializers.safety_resource_centre import SafetyResourceCentreSerializer


class CreateSafetyResourceCentreView(CreateAPIView):
    serializer_class = SafetyResourceCentreSerializer
    permission_classes = (AllowAny,)


class GetSafetyResourceCentreView(APIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = SafetyResourceCentreSerializer

    def get(self,*args,**kwargs):
        queryset = SafetyResourceCentre.objects.all().first()
        serializer = self.serializer_class(instance=queryset)
        return Response(serializer.data)