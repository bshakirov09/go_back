from rest_framework.generics import get_object_or_404
from food_dining.models.supermarket import SuperMarket
from rest_framework.response import Response


def delete_supermarket(pk: int) -> Response:
    """
    :param pk:
    :return:
    """
    instance: SuperMarket = get_object_or_404(SuperMarket, pk=pk)
    instance.delete()
    return Response(status=204)
