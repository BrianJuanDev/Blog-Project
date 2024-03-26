from django.shortcuts import render, get_object_or_404
from .models import Post
# from django.http import Http404
# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(request, 'templates/index.html', {'posts': posts})

def post_detail(request, id):
    #try:
    #   post = Post.published.get(id=id)
    #except Post.DoesNotExist:
    #   raise Http404('No post found')
    #return render(request, '', {'post': post})
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.status.PUBLISHED)
    
    return render(request, 'templates/post_detail.html', {'post_detail': post})