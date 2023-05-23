from django.urls import path
from apps.dashboards import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # categories
    path("categories/", views.dash_categories, name="dash_categories"),
    path("categories/add/", views.dash_category_add, name="dash_category_add"),
    path(
        "categories/edit/<int:pk>", views.dash_category_edit, name="dash_category_edit"
    ),
    path(
        "categories/delete/<int:pk>",
        views.dash_category_delete,
        name="dash_category_delete",
    ),
    # blog post
    path("posts/", views.dash_posts, name="dash_posts"),
    path("posts/add/", views.dash_post_add, name="dash_post_add"),
    path("posts/edit/<int:pk>", views.dash_post_edit, name="dash_post_edit"),
    path("posts/delete/<int:pk>", views.dash_post_delete, name="dash_post_delete"),
    # manage users
    path("users/", views.dash_users, name="dash_users"),
    path("users/add/", views.dash_user_add, name="dash_user_add"),
]
