from django.urls import path, register_converter
from .converter import DateConverter
from . import views

register_converter(DateConverter, 'date')

urlpatterns = [
    path('', views.get_products),
    path('create', views.create_product),
    path('findByStatus/<str:product_status>', views.get_product_by_is_active_status),
    path('findByTags/<str:product_tags>', views.get_product_by_tags),
    path('<int:product_id>', views.get_product_by_id),
    path('<int:product_id>/update', views.update_product),
    path('<int:product_id>/delete', views.delete_product),
    path('order/', views.get_order),
    path('order/create', views.create_order),
    path('<int:order_id>/update', views.update_order),
    path('findByStartDate/<date:start_date>', views.get_order_by_start_date),
    path('findByOrderedDate/<date:ordered_date>', views.get_order_by_ordered_date),
]