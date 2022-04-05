# Django
from django.urls import path, include

# Rest-Framework
from rest_framework.routers import DefaultRouter

# Views
from food_dining.views.take_out import (
    TakeOutCreateView,
    TakeOutUpdateView,
    TakeOutHasUpdateView,
    TakeOutFoodTypeUpdateView,
    TakeOutServiceOptionUpdateView,
    TakeOutMediaUpdateView,
    TakeOutOrderSitesUpdateView,
    TakeOutMealViewSet,
    TakeOutMenuViewSet,
    TakeOutListDetailViewSet,
    TakeOutDeleteView
)

router = DefaultRouter()
router.register('', TakeOutListDetailViewSet, '')
router.register('menu', TakeOutMenuViewSet, 'menu')
router.register('meal', TakeOutMealViewSet, 'meal')

urlpatterns = [
    path('take_out/create/', TakeOutCreateView.as_view()),
    path('take_out/update/<int:pk>/', TakeOutUpdateView.as_view()),
    path('take_out/update_has/<int:pk>/', TakeOutHasUpdateView.as_view()),
    path('take_out/update_food_type/<int:pk>/', TakeOutFoodTypeUpdateView.as_view()),
    path('take_out/update_service_option/<int:pk>/', TakeOutServiceOptionUpdateView.as_view()),
    path('take_out/update_order_site/<int:pk>/', TakeOutOrderSitesUpdateView.as_view()),
    path('take_out/update_media/<int:pk>/', TakeOutMediaUpdateView.as_view()),
    path('take_out/delete/<int:pk>/', TakeOutDeleteView.as_view()),
]
urlpatterns += [path('take_out/', include(router.urls))]
