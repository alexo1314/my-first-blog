from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post, About, Contacto
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, ContactoForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), title='Portafolio').order_by('-published_date')[:1]
    postsa2 = Post.objects.filter(published_date__lte=timezone.now(), title='Casamientos').order_by('-published_date')[:1]
    postsa3 = Post.objects.filter(published_date__lte=timezone.now(), title='Conciertos').order_by('-published_date')[:1]
    return render(request, 'blog/post_list.html', {'posts': posts, 'postsa2': postsa2, 'postsa3': postsa3})



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


def post_postb(request):
    postb = Post.objects.filter(title='Portafolio').order_by('-published_date')
    return render(request, 'blog/post_postb.html', {'post': postb})

def post_postc(request):
    postc = Post.objects.filter(title='Casamientos').order_by('-published_date')
    return render(request, 'blog/post_postc.html', {'post': postc})

def post_postd(request):
    postd = Post.objects.filter(title='Conciertos').order_by('-published_date')
    return render(request, 'blog/post_postd.html', {'post': postd})


def about(request):
    post = About.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:1]
    return render(request, 'blog/about.html', {'post': post})

def contacto(request):
    data ={
        'form' : ContactoForm()
    }
    if request.POST:
        contacto = Contacto()
        contacto.name = request.POST.get('txtname')
        contacto.email = request.POST.get('txtemail')
        contacto.text = request.POST.get('txtmessage')

        try:
            contacto.save()
            data['mensaje'] = 'Mensaje enviado'
        except:
            data['mensaje'] = 'Error al enviar el mensaje'
    return render(request, 'blog/contact.html', data)