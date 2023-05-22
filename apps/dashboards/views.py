from django.shortcuts import render

from apps.blogs.models import Blog, Category


# Create your views here.
def dashboard(request):
    """
    main dashboard
    """
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {"category_count": category_count, "blogs_count": blogs_count}
    return render(request, "dashboards/dashboard.html", context)
