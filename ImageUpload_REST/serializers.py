from rest_framework import serializers
from ImageUpload.models import UploadedImage

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UploadedImage
        fields = ('pk', 'image')