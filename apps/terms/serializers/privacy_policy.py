#Rest Framework
from rest_framework import serializers
#Project
from terms.models.privacy_policy import PrivacyPolicy


class PrivacyPolicySerializer(serializers.ModelSerializer):

    class Meta:
        model = PrivacyPolicy
        fields = ("description",)

    def create(self, validated_data):
        PrivacyPolicy.objects.update_or_create(
            pk=1, defaults=dict(description=validated_data["description"])
        )
        return validated_data