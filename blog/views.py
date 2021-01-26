from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    postsa2 = Post.objects.filter(published_date__lte=timezone.now(), title='llama2').order_by('-published_date')[:1]
    return render(request, 'blog/post_list.html', {'posts': posts, 'llamas': postsa2})


# Create your views here.
def post_lista(request):
    postsa = Post.objects.filter(published_date__lte=timezone.now(), title='llama1').order_by('-published_date')[:1]
    postsa2 = Post.objects.filter(published_date__lte=timezone.now(), title='llama2').order_by('-published_date')[:1]
    print(postsa)

    return render(request, 'blog/post_lista.html', {'postsa': postsa, 'llamas': postsa2})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

