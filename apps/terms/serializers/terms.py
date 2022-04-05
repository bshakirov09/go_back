#Rest Framework
from rest_framework import serializers
#Project
from terms.models.terms import Terms


class TermsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Terms
        fields=('description',)

    def create(self,validated_data):
        Terms.objects.update_or_create(
            pk=1,defaults=dict(description=validated_data["description"])
        )
        return validated_data

















