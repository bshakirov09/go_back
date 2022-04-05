# Rest-Framework
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Models
from food_dining.models.take_out import TakeOut


def delete_takeout(pk: int) -> Response:
    take_out: TakeOut = get_object_or_404(TakeOut, pk=pk)
    take_out.delete()
    return Response(status=204)
