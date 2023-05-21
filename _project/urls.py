"""
Project's URL
"""
from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from django.conf import settings

from _project import views
from apps.blogs import views as blog_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("category/", include("apps.blogs.urls")),
    path("<slug:slug>/", blog_views.blog_detail, name="blog_detail"),
    path("blogs/search/", blog_views.blog_search, name="blog_search"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
