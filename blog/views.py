from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView



def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post,
                            id=id,
                            status=Post.Status.PUBLISHED)
    
    return render(request, 'blog/post/detail.html', {'post': post})





class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'