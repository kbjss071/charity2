from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Post
from comments.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

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


class PostList(SelectRelatedMixin, generic.ListView):
    model = Post
    # need to know what select_related is
    select_related=("user")


class UserPosts(generic.ListView):
    model = Post
    template_name = "posts/user_post_list.html"

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact = self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise
        return super().get_queryset()