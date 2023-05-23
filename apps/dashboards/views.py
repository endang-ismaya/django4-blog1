from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

from apps.blogs.models import Blog, Category
from apps.dashboards.forms import AddUserForm, BlogPostForm, CategoryForm, EditUserForm
from apps.users.utils import is_post


@login_required(login_url="users_login")
def dashboard(request):
    """
    main dashboard
    """
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {
        "category_count": category_count,
        "blogs_count": blogs_count,
        "nav_dashboard": "bg-warning",
    }
    return render(request, "dashboards/dashboard.html", context)


@login_required(login_url="users_login")
def dash_categories(request):
    """
    show categories dashboard
    """
    context = {"nav_dash_categories": "bg-warning"}
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

    context = {"nav_dash_categories": "bg-warning", "form": form}
    return render(request, "dashboards/add-category.html", context)


@login_required(login_url="users_login")
def dash_category_edit(request, pk):
    """
    Handle edit category
    """
    category = get_object_or_404(Category, pk=pk)
    if is_post(request):
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("dash_categories")
    else:
        form = CategoryForm(instance=category)

    context = {
        "nav_dash_categories": "bg-warning",
        "form": form,
        "category": category,
    }
    return render(request, "dashboards/edit-category.html", context)


@login_required(login_url="users_login")
def dash_category_delete(request, pk):
    """
    Handle the deletion of Category
    """
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("dash_categories")


@login_required(login_url="users_login")
def dash_posts(request):
    posts = Blog.objects.all()

    context = {"nav_dash_blogs": "bg-warning", "posts": posts}
    return render(request, "dashboards/posts.html", context)


@login_required(login_url="users_login")
def dash_post_add(request):
    """
    Handle the addition of Blog Post
    """
    if is_post(request):
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            # temporary saving
            new_post = form.save(commit=False)

            # assign the author
            new_post.author = request.user
            new_post.save()  # save to get the id
            # assign the slug
            title = form.cleaned_data["title"] + "-" + str(new_post.id)
            new_post.slug = slugify(title)

            # save and redirect
            new_post.save()
            return redirect("dash_posts")
        else:
            print(form.errors)
    else:
        form = BlogPostForm()
    context = {"nav_dash_blogs": "bg-warning", "form": form}
    return render(request, "dashboards/add-post.html", context)


@login_required(login_url="users_login")
def dash_post_edit(request, pk):
    """
    Handle edit category
    """
    post = get_object_or_404(Blog, pk=pk)
    if is_post(request):
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            edited_post = form.save()
            title = form.cleaned_data["title"] + "-" + str(edited_post.id)
            edited_post.slug = slugify(title)
            edited_post.save()
            return redirect("dash_posts")
    else:
        form = BlogPostForm(instance=post)

    context = {
        "nav_dash_blogs": "bg-warning",
        "form": form,
        "post": post,
    }
    return render(request, "dashboards/edit-post.html", context)


@login_required(login_url="users_login")
def dash_post_delete(request, pk):
    """
    Handle the deletion of Post
    """
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect("dash_posts")


@login_required(login_url="users_login")
@permission_required("auth.view_user", login_url="users_login")
def dash_users(request):
    """
    To views all users
    """
    users = User.objects.all()
    context = {"nav_dash_users": "bg-warning", "users": users}
    return render(request, "dashboards/users.html", context)


@login_required(login_url="users_login")
@permission_required("auth.add_user", login_url="users_login")
def dash_user_add(request):
    """
    Handle the addition of a User
    """
    if is_post(request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dash_users")
        else:
            print(form.errors)
    else:
        form = AddUserForm()
    context = {"nav_dash_users": "bg-warning", "form": form}
    return render(request, "dashboards/add-user.html", context)


@login_required(login_url="users_login")
@permission_required("auth.change_user", login_url="users_login")
def dash_user_edit(request, pk):
    """
    Handle edit user
    """
    user = get_object_or_404(User, pk=pk)
    if is_post(request):
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("dash_users")
    else:
        form = EditUserForm(instance=user)

    context = {
        "nav_dash_users": "bg-warning",
        "form": form,
        "user": user,
    }
    return render(request, "dashboards/edit-user.html", context)


@login_required(login_url="users_login")
@permission_required("auth.delete_user", login_url="users_login")
def dash_user_delete(request, pk):
    """
    Handle the deletion of Post
    """
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect("dash_users")
