from django.shortcuts import get_object_or_404, redirect, render

from apps.blogs.models import Blog, Category


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
