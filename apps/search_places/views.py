from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.conf import settings

from search_places.serializers import ListMikVahSerializer, ShuLSerializer

from search_places.services.mikvah import Mikvah
from search_places.services.shuls import Shul


class ListMikVahView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        serializer = ListMikVahSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        return Mikvah.list_mik_vah(**serializer.validated_data)


class GetMikVahView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Mikvah.get_mik_vah(request.GET.get("id"))


class ListShuLView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        serializer = ShuLSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        request.META["app-id"] = settings.SHUL_APP_ID
        return Shul.list_shul(**serializer.validated_data)


class GetShuLView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        request.META["app-id"] = settings.SHUL_APP_ID
        return Shul.get_shul(request.GET.get("id"))
