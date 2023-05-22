from django.urls import path
from apps.users import views

urlpatterns = [
    path("register/", views.register, name="users_register"),
    path("login/", views.login, name="users_login"),
    path("logout/", views.logout, name="users_logout"),
]
