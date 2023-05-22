from django import forms

from apps.blogs.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("category_name",)
