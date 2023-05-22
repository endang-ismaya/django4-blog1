from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.blogs.models import Blog, Category
from apps.users.utils import get_sidebar_active


@login_required(login_url="users_login")
def dashboard(request):
    """
    main dashboard
    """
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    nav_dashboard = "bg-warning"

    context = {
        "category_count": category_count,
        "blogs_count": blogs_count,
        "nav_dashboard": nav_dashboard,
    }
    return render(request, "dashboards/dashboard.html", context)


@login_required(login_url="users_login")
def dash_categories(request):
    """
    show categories dashboard
    """
    nav_dash_categories = "bg-warning"
    context = {"nav_dash_categories": nav_dash_categories}
    return render(request, "dashboards/categories.html", context)


@login_required(login_url="users_login")
def dash_category_add(request):
    """
    Handle addition of Category
    """
    nav_dash_categories = "bg-warning"
    context = {"nav_dash_categories": nav_dash_categories}
    return render(request, "dashboards/add-category.html", context)
