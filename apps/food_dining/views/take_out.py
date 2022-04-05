# Rest-Framework
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView

# Project
from food_dining.models import TakeOutMenu, TakeOutMeal, TakeOut
from food_dining.serializers.base import (
    ItHasSelectSerializer,
    FoodTypeSelectSerializer,
    ServiceOptionSelectSerializer,
    MediaSelectSerializer,
    OrderSiteSelectSerializer,
)
from food_dining.serializers.take_out import (
    TakeOutCreateSerializer,
    TakeOutUpdateSerializer,
    TakeOutMenuSerializer,
    TakeOutMealSerializer,
    TakeOutSerializer,
    TakeOutDetailSerializer,
)

# Service
from food_dining.services.take_out.create import create_take_out
from food_dining.services.take_out.delete import delete_takeout
from food_dining.services.take_out.update import (
    update_take_out,
    update_takeout_has,
    update_takeout_food_type,
    update_takeout_service_option,
    update_takeout_media,
    update_takeout_order_sites,
)


class TakeOutCreateView(APIView):
    serializers_class = TakeOutCreateSerializer

    def post(self, request):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return create_take_out(**serializer.validated_data)


class TakeOutUpdateView(APIView):
    serializers_class = TakeOutUpdateSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_take_out(pk=pk, **serializer.validated_data)


class TakeOutDeleteView(APIView):
    delete_service = delete_takeout

    def delete(self, request, pk):
        return self.delete_service(pk=pk)


class TakeOutListDetailViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = TakeOut.objects.all()
    serializer_class = TakeOutSerializer
    detail_serializer_class = TakeOutDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = self.detail_serializer_class
        return super(TakeOutListDetailViewSet, self).retrieve(request, *args, **kwargs)


class TakeOutMenuViewSet(ModelViewSet):
    queryset = TakeOutMenu.objects.all()
    serializer_class = TakeOutMenuSerializer
    filter_fields = ['take_out', ]


class TakeOutMealViewSet(ModelViewSet):
    queryset = TakeOutMeal.objects.all()
    serializer_class = TakeOutMealSerializer
    filter_fields = ['menu', ]


class TakeOutHasUpdateView(APIView):
    serializers_class = ItHasSelectSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_takeout_has(pk, **serializer.validated_data)


class TakeOutFoodTypeUpdateView(APIView):
    serializers_class = FoodTypeSelectSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_takeout_food_type(pk, **serializer.validated_data)


class TakeOutServiceOptionUpdateView(APIView):
    serializers_class = ServiceOptionSelectSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_takeout_service_option(pk, **serializer.validated_data)


class TakeOutMediaUpdateView(APIView):
    serializers_class = MediaSelectSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_takeout_media(pk, **serializer.validated_data)


class TakeOutOrderSitesUpdateView(APIView):
    serializers_class = OrderSiteSelectSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_takeout_order_sites(pk, **serializer.validated_data)
