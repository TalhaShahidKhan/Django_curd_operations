from django.urls import path
from product.views import product_list,add_product,details_product,update_product,delt_product
urlpatterns = [
    path('',product_list,name="product_list"),
    path('addprod/',add_product,name="product_add"),
    path('detailprod/<pk>',details_product,name="product_det"),
    path('updateprod/<pk>',update_product,name="product_upd"),
    path('deleteprod/<pk>',delt_product,name="product_dlt"),
]

app_name='product'