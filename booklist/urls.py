from django.urls import path
from booklist.views import list_book
urlpatterns = [
    path('',list_book,name='listings')
]

app_name='booklist'