#Rest Framework
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
#Project
from terms.models.legal_notices import LegalNotices
from terms.serializers.legal_notices import LegalNoticesSerializer


class CreateLegalNoticesView(CreateAPIView):
    serializer_class = LegalNoticesSerializer
    permission_classes = (AllowAny,)


class GetLegalNoticesView(APIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = LegalNoticesSerializer

    def get(self,*args,**kwargs):
        queryset = LegalNotices.objects.all().first()
        serializer = self.serializer_class(instance=queryset)
        return Response(serializer.data)