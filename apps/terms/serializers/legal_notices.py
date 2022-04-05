#Rest Framework
from rest_framework import serializers
#Project
from terms.models.legal_notices import LegalNotices


class LegalNoticesSerializer(serializers.ModelSerializer):

    class Meta:
        model = LegalNotices
        fields = ("description",)

    def create(self, validated_data):
        LegalNotices.objects.update_or_create(
            pk=1, defaults=dict(description=validated_data["description"])
        )
        return validated_data
