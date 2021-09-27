# from .models import Product
from django.urls import path
from .views import *  #index

app_name  = "myapp"

urlpatterns = [
    path("brand/",showBrand,name="showBrand"),
    path("items/",showProduct,name="showProduct"),
    path("product/<int:id>/",one_product,name="name"),
    path("filter/",filtered_product,name="filter"),
    path("",index,name="name"),
]