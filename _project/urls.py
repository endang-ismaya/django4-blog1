"""
Project's URL
"""
from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from django.conf import settings

from _project import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("category/", include("apps.blogs.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
