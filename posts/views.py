from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Post

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

    return render(request, 'post_detail.html', context)
