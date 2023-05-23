from django import forms

from apps.blogs.models import Blog, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("category_name",)


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = (
            "author",
            "slug",
        )
