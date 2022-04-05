# Rest-Framework
from rest_framework import serializers

# Project
from file.serializers import FileSerializer
from user.models import User


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'phone_number',
            'gender',
            'birthday',
            'social_network',
            'city',
        ]

    def to_representation(self, instance):
        self.fields['avatar'] = FileSerializer(context=self.context)
        return super(UserMeSerializer, self).to_representation(instance)
