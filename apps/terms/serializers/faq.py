#Rest Framework
from rest_framework import serializers
#Project
from terms.models.faq import FAQ


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = ("description",)

    def create(self, validated_data):
        FAQ.objects.update_or_create(
            pk=1, defaults=dict(description=validated_data["description"])
        )
        return validated_data