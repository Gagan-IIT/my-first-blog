from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

"""
#This is one way for post_detail. Here, _posts will either be an empty object or a single object.
#We make a list of it and send to normal post_list.html. Another method is given after it.
def post_detail(request, pk):
    _posts = Post.objects.get(pk=pk)
    if isinstance(_posts, list):
        posts = _posts[:]
    else:
        posts = []
        posts.append(_posts)
    return render(request, 'blog/post_list.html', {'posts':posts})
    """

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})