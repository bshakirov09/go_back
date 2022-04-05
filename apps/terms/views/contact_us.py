#Rest Framework
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
#Project
from terms.models.contact_us import ContactUs
from terms.serializers.contact_us import ContactUsSerializer


class CreateContactUsView(CreateAPIView):
    serializer_class = ContactUsSerializer
    permission_classes = (AllowAny,)


class GetContactUsView(APIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = ContactUsSerializer

    def get(self,*args,**kwargs):
        queryset = ContactUs.objects.all().first()
        serializer = self.serializer_class(instance=queryset)
        return Response(serializer.data)

