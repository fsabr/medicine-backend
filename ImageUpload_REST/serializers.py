from rest_framework import serializers
from ImageUpload.models import UploadedImage, Base64

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UploadedImage
        fields = ('pk', 'image')

class Base64Serializer(serializers.ModelSerializer):
    class Meta:
        model  = Base64
        fields = ('pk', 'image') 