import requests
from rest_framework import status
from rest_framework.response import Response


class Mikvah:
    base_url = "https://www.mikvah.org/api/v1/"

    @staticmethod
    def list_mik_vah(latitude, longitude):
        data = requests.get(f"{Mikvah.base_url}/search/{latitude}/{longitude}").json()
        if not data.get("success"):
            return Response({"detail": "Something is wrong!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result": data.get("result")}, status=status.HTTP_200_OK)

    @staticmethod
    def get_mik_vah(id):
        data = requests.get(f"{Mikvah.base_url}/mikvah/{id}").json()
        if not id:
            return Response({"detail": "Id is missing!"}, status=status.HTTP_400_BAD_REQUEST)
        if not data.get("success"):
            return Response({"detail": "Something is wrong!"}, status=status.HTTP_400_BAD_REQUEST)
        result = data.get("result")
        return Response({key: value for key, value in result.items()}, status=status.HTTP_200_OK)
