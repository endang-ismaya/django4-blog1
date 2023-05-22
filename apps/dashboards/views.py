from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from apps.blogs.models import Blog, Category
from apps.dashboards.forms import CategoryForm
from apps.users.utils import is_post


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
    if is_post(request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dash_categories")
    else:
        form = CategoryForm()

    nav_dash_categories = "bg-warning"
    context = {"nav_dash_categories": nav_dash_categories, "form": form}
    return render(request, "dashboards/add-category.html", context)
