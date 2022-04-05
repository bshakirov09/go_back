from rest_framework import serializers


class ResendVerifyCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
