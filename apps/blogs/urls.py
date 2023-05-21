from django.urls import path
from apps.blogs import views

urlpatterns = [
    path("<int:category_id>", views.posts_by_category, name="posts_by_category"),
]
