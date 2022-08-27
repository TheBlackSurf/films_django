from typing import List
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth import get_user_model
from films.forms import RegisterForm
from django.views.generic.list import ListView
from .models import Film
from django.views.decorators.csrf import csrf_exempt


def search_film(request):
    search_text = request.POST.get('search')
    films = Film.objects.filter(title__icontains=search_text)
    return render(request, 'partials/search-result.html', {'films': films})


def film_list(request):
    films = Film.objects.all()
    return render(request, 'films.html', {
        'films': films
    })


def add_film(request):
    title = request.POST.get('title')
    if len(title) >= 2:
        Film.objects.create(title=title)

    films = Film.objects.all()
    return render(request, 'partials/list-film.html', {
        'films': films
    })


def delete_film(request, pk):
    film = Film.objects.get(id=pk)
    film.delete()
    films = Film.objects.all()
    return render(request, 'partials/list-film.html', {
        'films': films
    })


def change_status(request, pk):
    film = Film.objects.get(id=pk)
    if film.completed == True:
        film = Film.objects.filter(id=pk).update(completed=False)
    else:
        film = Film.objects.filter(id=pk).update(completed=True)
    films = Film.objects.all()
    return render(request, 'partials/list-film.html', {
        'films': films
    })


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div style='color:red'>This username already exist</div>")
    else:
        return HttpResponse("<div style='color:green'>This username is avilable</div>")


def check_password(request):
    password = request.POST.get('password1')
    return HttpResponse("Twoje hasło to " + password)


def check_title(request):
    title = request.POST.get('title')
    if len(title) < 2:
        return HttpResponse("<div style='color:red'>Tytuł jest za krótki</div>")
    else:
        return HttpResponse("<div style='color:green'>Idealna długość tytułu</div>")


class IndexView(TemplateView):
    template_name = 'index.html'


class Login(LoginView):
    template_name = 'registration/login.html'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)
