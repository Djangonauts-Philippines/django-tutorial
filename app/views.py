from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from .models import Post
from .forms import PostForm


def landing_page(request):
    """
    Landing page view that displays recent posts.
    """
    # Get the most recent published posts
    recent_posts = Post.objects.filter(is_published=True)[:6]

    # Get featured posts (most recent 3)
    featured_posts = recent_posts[:3] if recent_posts else []

    context = {
        "recent_posts": recent_posts,
        "featured_posts": featured_posts,
        "total_posts": Post.objects.filter(is_published=True).count(),
    }

    return render(request, "app/landing.html", context)


def post_detail(request, slug):
    """
    View to display individual post details.
    """
    post = get_object_or_404(Post, slug=slug, is_published=True)
    context = {"post": post}

    return render(request, "app/post_detail.html", context)


def all_posts(request):
    """
    View to display all published posts with pagination.
    """
    posts_list = Post.objects.filter(is_published=True)
    total_posts = posts_list.count()

    # Paginate the posts
    paginator = Paginator(posts_list, 10)  # Show 10 posts per page
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    context = {
        "posts": posts,
        "total_posts": total_posts,
    }
    return render(request, "app/all_posts.html", context)


@login_required
def create_post(request):
    """
    View to create a new post.
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()

    context = {"form": form}
    return render(request, "app/create_post.html", context)


@login_required
def delete_post(request, slug):
    """
    View to delete a post. Only the post author can delete their own posts.
    """
    post = get_object_or_404(Post, slug=slug)

    # Check if the current user is the author of the post
    if post.author != request.user:
        raise Http404("You don't have permission to delete this post.")

    if request.method == "POST":
        post_title = post.title
        post.delete()
        messages.success(request, f"Post '{post_title}' has been deleted successfully.")
        return redirect("app:landing")

    # If GET request, show confirmation page
    context = {"post": post}
    return render(request, "app/delete_post.html", context)


@login_required
def logout_view(request):
    """
    Logout view that logs out the user and redirects to landing page.
    """
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect("app:landing")
