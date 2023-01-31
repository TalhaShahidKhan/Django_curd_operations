from django.urls import path
from booklist.views import list_book,create_book
urlpatterns = [
    path('',list_book,name='listings'),
    path('addbook/',create_book,name='addbook'),
]

app_name='booklist'