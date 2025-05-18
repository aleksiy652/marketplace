from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


@login_required
def home(request):
    tovari = Tovar.objects.all()
    object = render(request, "home.html", {"products": tovari})
    return object


def register(request):
    if request.method == "GET":
        form = Register_form()
        object = render(request, "register.html", {"form": form})
        return object
    elif request.method == "POST":
        form = Register_form(request.POST)
        if form.is_valid():
            save_user = form.save()
            Karzina.objects.create(uzer=save_user)
            object = redirect("login")
            return object
        else:
            object = render(request, "register.html", {"form": form})
            return object


def tovar(request, id):
    chukcha = Tovar.objects.get(id=id)
    object = render(request, "page_tovarkus.html", {"tovar": chukcha})
    return object


def korzina(request):
    if request.user.is_authenticated:
        tavari = Karzina_Tovar.objects.filter(karzina=request.user.korzina)
        object = render(request, "korzuna.html", {"tavari": tavari})
        return object
    else:
        object = render(request, "net_korzinbI.html")
        return object


def add_korzin(request):
    id = request.POST["id"]
    tavar = Tovar.objects.get(id=id)
    tavar.kolvo -= 1
    tavar.save()
    request.user.korzina.tavari.add(tavar)
    object = redirect("main")
    return object


def plus(request):
    id = request.POST["id"]
    tavar = Tovar.objects.get(id=id)
    tik = Karzina_Tovar.objects.get(tovar=tavar, karzina=request.user.korzina)
    tik.kolvo += 1
    tavar.kolvo -= 1
    tik.save()
    tavar.save()
    object = redirect("korzina")
    return object


def minus(request):
    id = request.POST["id"]
    tavar = Tovar.objects.get(id=id)
    tik = Karzina_Tovar.objects.get(tovar=tavar, karzina=request.user.korzina)
    tik.kolvo -= 1
    tavar.kolvo += 1
    if tik.kolvo > 0:
        tik.save()
    else:
        request.user.korzina.tavari.remove(tavar)
    tavar.save()
    object = redirect("korzina")
    return object


def del_korzin(request):
    id = request.POST["id"]
    tavar = Tovar.objects.get(id=id)
    tik = Karzina_Tovar.objects.get(tovar=tavar, karzina=request.user.korzina)
    tavar.kolvo += tik.kolvo
    tavar.save()
    request.user.korzina.tavari.remove(tavar)

    object = redirect("korzina")
    return object


def user_login(request):
    if request.method == "GET":
        object = render(request, 'login.html')
        return object
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        chukcha = authenticate(request, username=username, password=password)
        if chukcha is not None:
            login(request, chukcha)
            return redirect('main')
        else:
            object = render(request, 'login.html')
            return object


def user_logout(request):
    logout(request)
    return redirect("login")


def profile(request):
    if request.method == "GET":
        form = Profile_form(instance=request.user)
        object = render(request, "profile.html", {"form": form})
        return object
    elif request.method == "POST":
        form = Profile_form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            object = redirect("profile")
            return object
        else:
            object = render(request, "profile.html", {"form": form})
            return object
