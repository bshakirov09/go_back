from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from food_dining.serializers.supermarket import *
from food_dining.models.supermarket import *
from food_dining.serializers.base import *
from food_dining.services.supermarket.create_supermarket import create_supermarket
from food_dining.services.supermarket.update_supermarket import *
from food_dining.services.supermarket.delete_supermarket import delete_supermarket


class SuperMarketCreateView(APIView):
    def post(self, request):
        serializer = SuperMarketCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return create_supermarket(**serializer.validated_data, creator=request.user)


class SuperMarketListView(ListAPIView):
    queryset = SuperMarket.objects.all()
    serializer_class = SuperMarketListSerializer


class SuperMarketDetailView(RetrieveAPIView):
    queryset = SuperMarket.objects.all()
    serializer_class = SuperMarketDetailSerializer


class SuperMarketMenuModelViewSet(ModelViewSet):
    queryset = SuperMarketMenu.objects.all()
    serializer_class = SuperMarketMenuModelSerializer
    filter_fields = ['supermarket']


class SuperMarketMealModelViewSet(ModelViewSet):
    queryset = SuperMarketMeal.objects.all()
    serializer_class = SuperMarketMealModelSerializer
    filter_fields = ['menu__supermarket']


class SuperMarketUpdateView(APIView):
    def post(self, request, pk):
        serializer = SupermarketUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_supermarket(**serializer.validated_data, pk=pk)


class SuperMarketHasUpdateView(APIView):

    def post(self, request, pk):
        serializer = ItHasSelectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_has(pk, **serializer.validated_data)


class SuperMarketFoodTypeUpdateView(APIView):

    def post(self, request, pk):
        serializer = FoodTypeSelectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_food_type(pk=pk, **serializer.validated_data)


class SuperMarketServiceOptionUpdateView(APIView):

    def post(self, request, pk):
        serializer = ServiceOptionSelectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_service_option(pk=pk, **serializer.validated_data)


class SuperMarketOrderSiteUpdateView(APIView):

    def post(self, request, pk):
        serializer = OrderSiteSelectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_order_site(pk=pk, **serializer.validated_data)


class SuperMarketFileUpdateView(APIView):

    def post(self, request, pk):
        serializer = MediaSelectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_media(pk, **serializer.validated_data)


class SuperMarketDeleteView(APIView):

    def delete(self, request, pk):
        return delete_supermarket(pk)


__all__ = [
    'SuperMarketCreateView',
    'SuperMarketListView',
    'SuperMarketMenuModelViewSet',
    'SuperMarketMealModelViewSet',
    'SuperMarketDetailView',
    'SuperMarketUpdateView',
    'SuperMarketHasUpdateView',
    'SuperMarketFoodTypeUpdateView',
    'SuperMarketServiceOptionUpdateView',
    'SuperMarketOrderSiteUpdateView',
    'SuperMarketFileUpdateView',
    'SuperMarketDeleteView'
]
