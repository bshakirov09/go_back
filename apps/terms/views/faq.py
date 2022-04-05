#Rest Framework
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
#Project
from terms.models.faq import FAQ
from terms.serializers.faq import FAQSerializer


class CreateFAQView(CreateAPIView):
    serializer_class = FAQSerializer
    permission_classes = (AllowAny,)


class GetFAQView(APIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = FAQSerializer

    def get(self,*args,**kwargs):
        queryset = FAQ.objects.all().first()
        serializer = self.serializer_class(instance=queryset)
        return Response(serializer.data)