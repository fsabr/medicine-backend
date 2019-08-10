from django.conf.urls import url
from django.urls import path
from .views import forum

urlpatterns = [
    path('forum/', forum)
]