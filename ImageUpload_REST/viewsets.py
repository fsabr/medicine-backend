from rest_framework import viewsets, filters
from .serializers import UploadedImageSerializer
from ImageUpload.models import UploadedImage

class UploadedImageViewset(viewsets.ModelViewSet):
    queryset         = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer