from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class LoginSocialNetworkSerializer(serializers.Serializer):
    GOOGLE = 'google'
    FACEBOOK = 'facebook'
    TYPE_TOKEN = ((GOOGLE, GOOGLE), (FACEBOOK, FACEBOOK))
    access_token = serializers.CharField()
    type_token = serializers.ChoiceField(TYPE_TOKEN)
