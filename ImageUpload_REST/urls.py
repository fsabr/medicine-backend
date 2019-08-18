from django.conf.urls import url, include
from rest_framework import routers
from .viewsets import UploadedImageViewset
from .views import scanner
from django.urls import path


router = routers.DefaultRouter()
router.register('image', UploadedImageViewset, 'image')

urlpatterns = [
    path('medimg/', scanner),
    url(r'^', include(router.urls))
]