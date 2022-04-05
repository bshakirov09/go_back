# Rest-Framework
from rest_framework.views import APIView

# Project
from food_dining.serializers.food_service import (
    FoodServiceCreateSerializer,
    FoodServiceUpdateSerializer
)
from food_dining.services.food_service.create import create_food_service
from food_dining.services.food_service.update import (
    update_food_service,
)


class FoodServiceCreateView(APIView):
    serializers_class = FoodServiceCreateSerializer

    def post(self, request):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return create_food_service(**serializer.validated_data)


class FoodServiceUpdateView(APIView):
    serializers_class = FoodServiceUpdateSerializer

    def post(self, request, pk):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_food_service(pk=pk, **serializer.validated_data)
