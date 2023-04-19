from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_products),
    path('create', views.create_product),
    path('findByStatus/<str:product_status>', views.get_product_by_status),
    path('findByTags/<str:product_tags>', views.get_product_by_tags),
]