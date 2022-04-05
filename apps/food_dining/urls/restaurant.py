# Django
from django.urls import path, include

# Rest-Framework
from rest_framework.routers import DefaultRouter

# Views
from food_dining.views.restaurant import (
    RestaurantCreateView,
    RestaurantMenuViewSet,
    RestaurantMealViewSet,
    RestaurantUpdateView,
    RestaurantHasUpdateView,
    RestaurantGoodForUpdateView,
    RestaurantFoodTypeUpdateView,
    RestaurantServiceOptionUpdateView,
    RestaurantOrderSitesUpdateView,
    RestaurantReserveSitesUpdateView,
    RestaurantMediaUpdateView,
    RestaurantDeleteView,
    RestaurantListDetailViewSet
)

router = DefaultRouter()
router.register('', RestaurantListDetailViewSet, '')
router.register('menu', RestaurantMenuViewSet, 'menu')
router.register('meal', RestaurantMealViewSet, 'meal')

urlpatterns = [
    path('restaurant/create/', RestaurantCreateView.as_view()),
    path('restaurant/update/<int:pk>/', RestaurantUpdateView.as_view()),
    path('restaurant/update_has/<int:pk>/', RestaurantHasUpdateView.as_view()),
    path('restaurant/update_good_for/<int:pk>/', RestaurantGoodForUpdateView.as_view()),
    path('restaurant/update_food_type/<int:pk>/', RestaurantFoodTypeUpdateView.as_view()),
    path('restaurant/update_service_option/<int:pk>/', RestaurantServiceOptionUpdateView.as_view()),
    path('restaurant/update_order_site/<int:pk>/', RestaurantOrderSitesUpdateView.as_view()),
    path('restaurant/update_reserve_site/<int:pk>/', RestaurantReserveSitesUpdateView.as_view()),
    path('restaurant/update_media/<int:pk>/', RestaurantMediaUpdateView.as_view()),
    path('restaurant/delete/<int:pk>/', RestaurantDeleteView.as_view()),
]
urlpatterns += [path('restaurant/', include(router.urls))]
