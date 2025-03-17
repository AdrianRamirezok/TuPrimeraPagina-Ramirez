from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, BusquedaForm

def inicio(request):
    posts = Post.objects.all()
    return render(request, 'blog/inicio.html', {'posts': posts})


def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

def buscar(request):
    resultados = []
    if request.method == 'GET':
        form = BusquedaForm(request.GET)
        if form.is_valid():
            termino = form.cleaned_data['buscar']
            resultados = Post.objects.filter(titulo__icontains=termino)
    else:
        form = BusquedaForm()
    return render(request, 'blog/buscar.html', {'form': form, 'resultados': resultados})

def listar_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/listar_posts.html', {'posts': posts})

# Create your views here.
