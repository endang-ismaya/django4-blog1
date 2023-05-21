from django.shortcuts import get_object_or_404, redirect, render

from apps.blogs.models import Blog, Category
from django.db.models import Q


# Create your views here.
def posts_by_category(request, category_id):
    try:
        # fetch category by category_id
        category = Category.objects.get(pk=category_id)
        # fetch Blog by category_id
        posts = Blog.objects.filter(status="Published", category=category_id)

        context = {"posts": posts, "category": category}
        return render(request, "posts_by_category.html", context)
    except (Category.DoesNotExist, Blog.DoesNotExist) as e:
        print(e)
        return redirect("home")


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status="Published")
    context = {"blog": blog}
    return render(request, "blog-detail.html", context)


def blog_search(request):
    q = request.GET.get("q")
    posts = Blog.objects.filter(
        Q(title__icontains=q)
        | Q(short_description__icontains=q)
        | Q(blog_body__icontains=q),
        status="Published",
    )
    context = {"posts": posts, "term": q}
    return render(request, "blog-search.html", context)
