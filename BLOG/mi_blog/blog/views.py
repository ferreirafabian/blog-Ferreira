from django.shortcuts import render
from blog.forms import AutorForm, CategoriaForm, PostForm, BusquedaForm
from blog.models import Post

def inicio(request):
    return render(request, "blog/inicio.html")

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "blog/exito.html")
    else:
        form = AutorForm()
    return render(request, "blog/form_autor.html", {"form": form})

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "blog/exito.html")
    else:
        form = CategoriaForm()
    return render(request, "blog/form_categoria.html", {"form": form})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "blog/exito.html")
    else:
        form = PostForm()
    return render(request, "blog/form_post.html", {"form": form})

def buscar_post(request):
    resultado = None
    if request.GET.get("titulo"):
        titulo = request.GET["titulo"]
        resultado = Post.objects.filter(titulo__icontains=titulo)

    form = BusquedaForm()
    return render(request, "blog/buscar.html", {"form": form, "resultado": resultado})
