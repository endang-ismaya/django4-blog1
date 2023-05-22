from django.urls import path
from apps.dashboards import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("categories/", views.dash_categories, name="dash_categories"),
    path("categories/add/", views.dash_category_add, name="dash_category_add"),
]
