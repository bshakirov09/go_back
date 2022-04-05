from django.urls import path, include
from rest_framework.routers import DefaultRouter
from food_dining.views.bakery import *

router = DefaultRouter()
router.register('bakery_menu', BakeryMenuModelViewSet, 'bakery_menu')
router.register('bakery_meal', BakeryMealModelViewSet, 'bakery_meal')

urlpatterns = [
    path('bakery/create/', BakeryCreateView.as_view()),
    path('bakery/update/<int:pk>/', BakeryUpdateView.as_view()),
    path('bakery/update_has/<int:pk>/', BakeryHasUpdateView.as_view()),
    path('bakery/update_food_type/<int:pk>/', BakeryFoodTypeUpdateView.as_view()),
    path('bakery/update_service_option/<int:pk>/', BakeryServiceOptionUpdateView.as_view()),
    path('bakery/update_order_site/<int:pk>/', BakeryOrderSiteUpdateView.as_view()),
    path('bakery/delete/<int:pk>/', BakeryDeleteView.as_view()),
    path('bakery/update_photo/<int:pk>/', BakeryFileUpdateView.as_view()),
    path('bakery/list/', BakeryListView.as_view()),
    path('bakery/detail/<int:pk>/', BakeryDetailView.as_view()),
    path('', include(router.urls))
]
