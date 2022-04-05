from rest_framework import serializers


class ListMikVahSerializer(serializers.Serializer):
    latitude = serializers.CharField()
    longitude = serializers.CharField()


class ShuLSerializer(ListMikVahSerializer):
    page_number = serializers.IntegerField()
