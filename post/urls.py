from django.urls import path
from post.views import all_posts,create_post
urlpatterns = [
    path('',all_posts,name='post_list'),
    path('addpost',create_post,name='post_form'),
]

app_name='post'