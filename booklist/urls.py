from django.urls import path
from booklist.views import list_book,create_book,update_book,delete_book,book_details
urlpatterns = [
    path('',list_book,name='listings'),
    path('addbook/',create_book,name='addbook'),
    path('detailbook/<pk>',book_details,name='detailbook'),
    path('updatebook/<pk>',update_book,name='up_book'),
    path('deletebook/<pk>',delete_book,name='del_book'),
]

app_name='booklist'