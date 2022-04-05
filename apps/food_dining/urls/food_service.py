# Django
from django.urls import path, include

# Rest-Framework
from rest_framework.routers import DefaultRouter

# Views
from food_dining.views.food_service import (
    FoodServiceCreateView,
    FoodServiceUpdateView
)

router = DefaultRouter()

urlpatterns = [
    path('food_service/create/', FoodServiceCreateView.as_view()),
    path('food_service/update/<int:pk>/', FoodServiceUpdateView.as_view())
]
urlpatterns += [path('food_service/', include(router.urls))]
