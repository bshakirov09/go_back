from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from food_dining.serializers.bakery import *
from food_dining.serializers.base import *
from food_dining.services.bakery.create_bakery import create_bakery
from food_dining.services.bakery.update_bakery import *
from food_dining.services.bakery.delete_bakery import delete_bakery
from food_dining.models.bakery import *


class BakeryCreateView(APIView):

    def post(self, request):
        serializer = BakeryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return create_bakery(**serializer.validated_data, creator=request.user)


class BakeryListView(ListAPIView):
    queryset = Bakery.objects.all()
    serializer_class = BakeryListSerializer


class BakeryDetailView(RetrieveAPIView):
    queryset = Bakery.objects.all()
    serializer_class = BakeryDetailSerializer


class BakeryMenuModelViewSet(ModelViewSet):
    queryset = BakeryMenu.objects.all()
    serializer_class = BakeryMenuModelSerializer
    filter_fields = ['bakery']


class BakeryMealModelViewSet(ModelViewSet):
    queryset = BakeryMeal.objects.all()
    serializer_class = BakeryMealModelSerializer
    filter_fields = ['menu__bakery']


class BakeryUpdateView(APIView):

    def post(self, request, pk):
        serializer = BakeryUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_bakery(**serializer.validated_data, pk=pk)


class BakeryHasUpdateView(APIView):

    def post(self, request, pk):
        serializer = ItHasSelectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_has(pk, **serializer.validated_data)


class BakeryFoodTypeUpdateView(APIView):

    def post(self, request, pk):
        serializer = FoodTypeSelectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_food_type(pk=pk, **serializer.validated_data)


class BakeryServiceOptionUpdateView(APIView):

    def post(self, request, pk):
        serializer = ServiceOptionSelectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_service_option(pk=pk, **serializer.validated_data)


class BakeryOrderSiteUpdateView(APIView):

    def post(self, request, pk):
        serializer = OrderSiteSelectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_order_site(pk=pk, **serializer.validated_data)


class BakeryFileUpdateView(APIView):

    def post(self, request, pk):
        serializer = MediaSelectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_media(pk, **serializer.validated_data)


class BakeryDeleteView(APIView):

    def delete(self, request, pk):
        return delete_bakery(pk)


__all__ = [
    'BakeryCreateView',
    'BakeryUpdateView',
    'BakeryHasUpdateView',
    'BakeryFoodTypeUpdateView',
    'BakeryServiceOptionUpdateView',
    'BakeryOrderSiteUpdateView',
    'BakeryMenuModelViewSet',
    'BakeryMealModelViewSet',
    'BakeryDeleteView',
    'BakeryFileUpdateView',
    'BakeryListView',
    'BakeryDetailView'
]
