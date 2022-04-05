# Rest
from rest_framework import serializers
# Project
from explore.models.explore import Explore, ExploreImage, Tag, ExploreTag
from file.models import File
from file.serializers import FileSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ExploreSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(many=True, queryset=File.objects.all(), write_only=True)
    tag = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), write_only=True)

    class Meta:
        model = Explore
        fields = [
            'id',
            'title',
            'description',
            'latitude',
            'longitude',
            'country',
            'city',
            'images',
            'tag'
        ]

    def create(self, validated_data):
        images = validated_data.pop('images')
        tags = validated_data.pop('tag')
        explore = Explore.objects.create(**validated_data)
        for tag in tags:
            ExploreTag.objects.create(explore=explore, tag=tag)
        for image in images:
            ExploreImage.objects.create(explore=explore, file=image)
        return explore

    def update(self, instance: Explore, validated_data):
        images = validated_data.get('images')
        tags = validated_data.get('tag')

        instance.title = validated_data['title']
        instance.description = validated_data['description']
        instance.latitude = validated_data['latitude']
        instance.longitude = validated_data['longitude']
        instance.city = instance.city
        instance.save()

        ExploreImage.objects.filter(explore=instance).delete()
        ExploreTag.objects.filter(explore=instance).delete()

        for image in images:
            ExploreImage.objects.create(explore=instance, file=image)
        for tag in tags:
            ExploreTag.objects.create(explore=instance, tag=tag)
        return instance


class ExploreRetrieveSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Explore
        fields = [
            'id',
            'title',
            'description',
            'images',
            'latitude',
            'longitude',
            'country',
            'city'
        ]

    def get_images(self, obj):
        images = obj.explore.all().order_by('file__ordering')
        images = [i.file for i in images]
        serializer = FileSerializer(images, many=True, context=self.context)
        return serializer.data


class ExploreListSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Explore
        fields = [
            'images',
            'city'
        ]

    def get_images(self, obj):
        image = obj.explore.filter(file__is_main=True).first()
        if image is None:
            return None
        serializer = FileSerializer(image.file, many=True, context=self.context)
        return serializer.data
