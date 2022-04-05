#Rest Framework
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
#Project
from terms.models.terms import Terms
from terms.serializers.terms import TermsSerializer


class CreateTermsView(CreateAPIView):
    serializer_class = TermsSerializer
    permission_classes = (AllowAny,)


class GetTermsView(APIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = TermsSerializer

    def get(self, *args, **kwargs):
        queryset = Terms.objects.all().first()
        serializer = self.serializer_class(instance=queryset)
        return Response(serializer.data)