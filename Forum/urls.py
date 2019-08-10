from django.conf.urls import url
from django.urls import path
from .views import forum, post_detail

urlpatterns = [
    path('forum/', forum),
    path('forum/<int:pk>', post_detail)
]