from django.urls import path
from post.views import all_posts
urlpatterns = [
    path('',all_posts,name='post_list'),
]

app_name='post'