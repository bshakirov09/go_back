#Rest Framework
from rest_framework import serializers
#Project
from terms.models.safety_resource_centre import SafetyResourceCentre


class SafetyResourceCentreSerializer(serializers.ModelSerializer):

    class Meta:
        model = SafetyResourceCentre
        fields = ("description",)

    def create(self, validated_data):
        SafetyResourceCentre.objects.update_or_create(
            pk=1, defaults=dict(description=validated_data["description"])
        )
        return validated_data