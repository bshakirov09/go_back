from rest_framework.generics import get_object_or_404
from food_dining.models.bakery import Bakery
from rest_framework.response import Response


def delete_bakery(pk: int) -> Response:
    """
    :param pk:
    :return:
    """
    instance: Bakery = get_object_or_404(Bakery, pk=pk)
    instance.delete()
    return Response(status=204)
