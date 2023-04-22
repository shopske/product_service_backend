from django.urls import path
from . import views


urlpatterns = [
    path('register', views.create_user),
    path('login', views.login_required),
    path('logout', views.logout_required),
    path('<str:user_name>', views.get_user_by_username),
    path('<str:user_name>/update', views.update_user),
    path('<str:user_name>/delete', views.delete_user),
]