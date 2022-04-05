# Django
from django.urls import path, include

# Rest-Framework
from rest_framework.routers import DefaultRouter

# Views
from food_dining.views import base

# Urls
from food_dining.urls.bakery import urlpatterns as bakery_urls
from food_dining.urls.restaurant import urlpatterns as restaurant_urls
from food_dining.urls.take_out import urlpatterns as take_out_urls
from food_dining.urls.supermarket import urlpatterns as supermarket_urls
from food_dining.urls.food_service import urlpatterns as food_service_urls

base_router = DefaultRouter()
base_router.register('food_type', base.FoodTypeViewSet, 'food-type')
base_router.register('service_option', base.ServiceOptionViewSet, 'service-option')
base_router.register('it_has', base.ItHasViewSet, 'it-has')
base_router.register('good_for', base.GoodForViewSet, 'good-for')
base_router.register('order_site_link', base.OrderSiteViewSet, 'good-for')
base_router.register('reserve_site_link', base.ReserveSiteViewSet, 'good-for')
base_router.register('working_hours', base.WorkingHoursUpdate, 'working-hours')

urlpatterns = [
    path('', include(base_router.urls))
]
urlpatterns += bakery_urls
urlpatterns += restaurant_urls
urlpatterns += take_out_urls
urlpatterns += supermarket_urls
urlpatterns += food_service_urls
