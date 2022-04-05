# Rest-Framework
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

# Project
from food_dining.models import RestaurantMenu, RestaurantMeal, Restaurant
from food_dining.serializers.restaurant.create import RestaurantCreateSerializer
from food_dining.serializers.restaurant.menu import RestaurantMenuSerializer, RestaurantMealSerializer
from food_dining.serializers.restaurant.retrieve import RestaurantSerializer, RestaurantDetailSerializer
from food_dining.serializers.base import (
    ItHasSelectSerializer,
    GodForSelectSerializer,
    FoodTypeSelectSerializer,
    ServiceOptionSelectSerializer,
    MediaSelectSerializer,
    OrderSiteSelectSerializer,
    ReserveSiteSelectSerializer
)
from food_dining.serializers.restaurant.update import RestaurantUpdateSerializer
from food_dining.services.restaurant.create import create_restaurant
from food_dining.services.restaurant.delete import delete_restaurant
from food_dining.services.restaurant.update import (
    update_restaurant,
    update_restaurant_has,
    update_restaurant_good_for,
    update_restaurant_food_type,
    update_restaurant_service_option,
    update_restaurant_media,
    update_restaurant_reserve_sites,
    update_restaurant_order_sites,
)


class RestaurantCreateView(APIView):
    serializers_class = RestaurantCreateSerializer

    def post(self, request):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return create_restaurant(**serializer.validated_data)


class RestaurantUpdateView(APIView):
    serializers_class = RestaurantUpdateSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_restaurant(pk=pk, **serializer.validated_data)


class RestaurantListDetailViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    detail_serializer_class = RestaurantDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = self.detail_serializer_class
        return super(RestaurantListDetailViewSet, self).retrieve(request, *args, **kwargs)


class RestaurantDeleteView(APIView):
    delete_service = delete_restaurant

    def delete(self, request, pk):
        return self.delete_service(pk)


class RestaurantMenuViewSet(ModelViewSet):
    queryset = RestaurantMenu.objects.all()
    serializer_class = RestaurantMenuSerializer
    filter_fields = ['restaurant', ]


class RestaurantMealViewSet(ModelViewSet):
    queryset = RestaurantMeal.objects.all()
    serializer_class = RestaurantMealSerializer
    filter_fields = ['menu', ]


class RestaurantHasUpdateView(APIView):
    serializers_class = ItHasSelectSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_restaurant_has(pk, **serializer.validated_data)


class RestaurantGoodForUpdateView(APIView):
    serializers_class = GodForSelectSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_restaurant_good_for(pk, **serializer.validated_data)


class RestaurantFoodTypeUpdateView(APIView):
    serializers_class = FoodTypeSelectSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_restaurant_food_type(pk, **serializer.validated_data)


class RestaurantServiceOptionUpdateView(APIView):
    serializers_class = ServiceOptionSelectSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_restaurant_service_option(pk, **serializer.validated_data)


class RestaurantMediaUpdateView(APIView):
    serializers_class = MediaSelectSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_restaurant_media(pk, **serializer.validated_data)


class RestaurantOrderSitesUpdateView(APIView):
    serializers_class = OrderSiteSelectSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_restaurant_order_sites(pk, **serializer.validated_data)


class RestaurantReserveSitesUpdateView(APIView):
    serializers_class = ReserveSiteSelectSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_restaurant_reserve_sites(pk, **serializer.validated_data)
