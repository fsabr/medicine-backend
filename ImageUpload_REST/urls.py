from django.conf.urls import url, include
from rest_framework import routers
from .viewsets import UploadedImageViewset

router = routers.DefaultRouter()
router.register('image', UploadedImageViewset, 'image')

urlpatterns = [
    url(r'^', include(router.urls))
]