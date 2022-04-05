import requests
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime


class Shul:
    base_url = "https://www.godaven.com/api/V2/shuls"

    @staticmethod
    def list_shul(latitude, longitude, page_number):
        try:
            data = requests.get(
                f"{Shul.base_url}/radius-search?lat={latitude}&lng={longitude}&pagenumber={page_number}&"
                f"todays_day=1&current_time={datetime.now().strftime('%H:%M')}"
            ).json()
        except Exception:
            return Response({"detail": "Something is wrong!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"number_of_pages": data.get("num_of_pages"), "shuls": data.get("shuls")},
                            status=status.HTTP_200_OK)

    @staticmethod
    def get_shul(id):
        if not id:
            return Response({"detail": "Id is missing!"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            data = requests.get(f"{Shul.base_url}/{id}/details").json()
        except Exception as ex:
            return Response({"detail": "Something is wrong!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({key: value for key, value in data.items()}, status=status.HTTP_200_OK)
