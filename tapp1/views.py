from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request, 'tapp1/post/list.html', {'post':posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__mounth=mounth, publish__day=day)
    return render(request, 'tapp1/post/detail.html',{'post':post})
    
    