from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm

# This section contains views for different functionalities related to the blog.

def blog_index(request):
    # Retrieves all posts and orders them by creation date in descending order.
    posts = Post.objects.all().order_by("-created_on")

    context = {
        "posts": posts,
    }

    return render(request, "blog/index.html", context)


def blog_detail(request, pk):
    # Retrieves a specific post based on the primary key (pk) passed in the URL.
    post = Post.objects.get(pk=pk)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # Saves a new comment related to the post.
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    # Retrieves comments related to the post.
    comments = Comment.objects.filter(post=post)

    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),  # Passes an instance of the comment form to the context.
    }

    return render(request, "blog/detail.html", context)


def blog_category(request, category):
    # Retrieves posts belonging to a specific category and orders them by creation date in descending order.
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")

    context = {
        "category": category,
        "posts": posts,
    }

    return render(request, "blog/category.html", context)
