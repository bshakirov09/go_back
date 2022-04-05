#Rest Framework
from rest_framework import serializers
#Project
from terms.models.contact_us import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = ("description",)

    def create(self, validated_data):
        ContactUs.objects.update_or_create(
            pk=1, defaults=dict(description=validated_data["description"])
        )
        return validated_data