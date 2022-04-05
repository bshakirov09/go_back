# Rest-Framework
from rest_framework import serializers

# Model
from file.models import File
from user.models import User


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'gender',
            'email',
            'city',
            'birthday',
            'phone_number',
        ]
        extra_kwargs = {
            'phone_number': {
                'required': False,
                'allow_null': True,
                'allow_blank': True
            },
        }


class UserAvatarUpdateSerializer(serializers.Serializer):
    avatar = serializers.PrimaryKeyRelatedField(queryset=File.objects.all())
