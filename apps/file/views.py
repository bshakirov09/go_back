# Rest-Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

# Project
from .models import File
from .serializers import FileSerializer


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = (AllowAny,)

    # def get_serializer_context(self):
    #     context = super(FileViewSet, self).get_serializer_context()
    #     context.update({"request": self.request})
    #     return context