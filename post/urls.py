from django.urls import path
from post.views import all_posts,create_post,detail_post,update_post,delt_post
urlpatterns = [
    path('',all_posts,name='post_list'),
    path('addpost',create_post,name='post_form'),
    path('dpost/<pk>',detail_post,name='det_post'),
    path('updpost/<pk>',update_post,name='upd_post'),
    path('deltpost/<pk>',delt_post,name='del_post'),
]

app_name='post'