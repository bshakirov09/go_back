# Rest-Framework
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Models
from food_dining.models.restaurant import Restaurant


def delete_restaurant(pk: int) -> Response:
    instance: Restaurant = get_object_or_404(Restaurant, pk=pk)
    instance.delete()
    return Response(status=204)
