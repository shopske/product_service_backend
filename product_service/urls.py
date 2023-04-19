from django.urls import path
from . import views


urlpatterns = [
    path('product', views.get_products),
    path('product/create', views.create_product),
]