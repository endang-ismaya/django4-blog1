from django.urls import path
from apps.dashboards import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]
