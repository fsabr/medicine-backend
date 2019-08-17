from django.conf.urls import url
from django.urls import path
from .views import forum, post_detail, forum_category, new_comment

urlpatterns = [
    path('forum/', forum, name='forum'),
    path('forum/<int:pk>/', post_detail, name='post_detail'),
    path('forum/<str:category>/', forum_category, name='forum_category'),
    path('comment/', new_comment, name='new_comment')
]