from django.contrib import admin

from apps.blogs.models import Blog, Category


class BlogAmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "title",
        "category",
        "author",
        "status",
        "is_featured",
        "updated_at",
    )
    search_fields = ("id", "title", "category__category_name", "status")
    list_editable = (
        "is_featured",
        "status",
    )


admin.site.register(Category)
admin.site.register(Blog, BlogAmin)
