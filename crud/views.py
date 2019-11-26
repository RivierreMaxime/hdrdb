from django.shortcuts import render, redirect
from django.http import HttpResponse
from crud.forms import FilmForm
from crud.models import Film
# Create your views here.

def test(request):
    return HttpResponse("Ceci est un test")

#https://www.javatpoint.com/django-crud-example
def film(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        try:
            form.save()
            return redirect('/crud/show')
        except:
            pass
    else:
        form = FilmForm()
    return render(request, 'crud/index.html', {'form':form})
def edit(request, id):
    film = Film.objects.get(id=id)
    return render(request, 'crud/edit.html', {'film':film})
def show(request):
    films = Film.objects.all()
    return render(request, "crud/show.html", {'films':films})
def update(request, id):
    film = Film.objects.get(id=id)
    form = FilmForm(request.POST, instance=film)
    if form.is_valid():  
        form.save()  
        return redirect("/crud/show")
    return render(request, 'crud/edit.html', {'film': film})
def destroy(request, id):  
    film = Film.objects.get(id=id)
    film.delete()
    return redirect("/crud/show")  