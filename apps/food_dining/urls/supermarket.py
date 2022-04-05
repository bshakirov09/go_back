from django.urls import path, include
from rest_framework.routers import DefaultRouter
from food_dining.views.supermarket import *

router = DefaultRouter()
router.register('supermarket_menu', SuperMarketMenuModelViewSet, 'supermarket_menu')
router.register('supermarket_meal', SuperMarketMealModelViewSet, 'supermarket_meal')

urlpatterns = [
    path('supermarket/create/', SuperMarketCreateView.as_view()),
    path('supermarket/update/<int:pk>/', SuperMarketUpdateView.as_view()),
    path('supermarket/update_has/<int:pk>/', SuperMarketHasUpdateView.as_view()),
    path('supermarket/update_food_type/<int:pk>/', SuperMarketFoodTypeUpdateView.as_view()),
    path('supermarket/update_service_option/<int:pk>/', SuperMarketServiceOptionUpdateView.as_view()),
    path('supermarket/update_order_site/<int:pk>/', SuperMarketOrderSiteUpdateView.as_view()),
    path('supermarket/update_photo/<int:pk>/', SuperMarketFileUpdateView.as_view()),
    path('supermarket/delete/<int:pk>/', SuperMarketDeleteView.as_view()),
    path('supermarket/list/', SuperMarketListView.as_view()),
    path('supermarket/detail/<int:pk>/', SuperMarketDetailView.as_view()),
    path('', include(router.urls))
]
