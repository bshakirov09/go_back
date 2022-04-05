# Rest
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
# Project
from explore.serializers.explore import ExploreListSerializer, ExploreSerializer, ExploreRetrieveSerializer, \
    TagSerializer
from explore.models.explore import Explore, ExploreImage, Tag, ExploreTag
from file.models import File


class TagViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ExploreViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Explore.objects.all()
    serializer_class = ExploreSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ExploreListSerializer
        return super(ExploreViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = ExploreRetrieveSerializer
        return super(ExploreViewSet, self).retrieve(request, *args, **kwargs)
