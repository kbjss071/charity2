from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse, Http404
from comments.forms import CommentForm
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from .models import Post
from .forms import PostForm

from braces.views import SelectRelatedMixin

# Create your views here.

@require_POST
def donate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    amount = float(request.POST.get('amount'))

    if amount <= 0:
        return JsonResponse({'error': 'Invalid amount.'}, status=400)

    post.current_amount += amount
    post.save()

    return JsonResponse({'success': True})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    form = CommentForm

    return render(request, 'post_detail.html', context)


def post_list(request):
    queryset = Post.objects.all().select_related('user')
    context = {'object_list': queryset}
    return render(request, 'posts/post_list.html', context)


def user_posts(request, username):
    try:
        post_user = User.objects.prefetch_related("posts").get(
            username__iexact=username
        )
    except User.DoesNotExist:
        raise Http404("User does not exist")

    posts = post_user.posts.all()

    context = {"post_user": post_user, "posts": posts}
    return render(request, "posts/user_post_list.html", context)
    

@login_required
@require_http_methods(["GET", "POST"])
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'myapp/post_form.html', {'form': form})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Post created!")
            return redirect("posts:all")
    else:
        form = PostForm()

    return render(request, "posts/post_form.html", {"form": form})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.user:
        raise Http404

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted!")
        return redirect("posts:all")

    return render(request, "posts/post_confirm_delete.html", {"object": post})

def post_detail(request, username, pk):
    queryset = Post.objects.select_related("user", "group")
    post = get_object_or_404(queryset, pk=pk, user__username__iexact=username)
    return render(request, "posts/post_detail.html", {"post": post})
