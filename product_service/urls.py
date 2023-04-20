from django.urls import path
from . import views

app_name = "shopske"

urlpatterns = [
    path('', views.get_products),
    path('create', views.create_product),
    path('findByStatus/<str:product_status>', views.get_product_by_status),
    path('findByTags/<str:product_tags>', views.get_product_by_tags),
    path('<int:product_id>', views.get_product_by_id),
    path('<int:product_id>/update', views.update_product),
    path('<int:product_id>/delete', views.delete_product),
]