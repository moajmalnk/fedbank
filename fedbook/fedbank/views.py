from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import PersonForm
from django.http import JsonResponse
import json
from .models import Branch


def person(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('apply')
    return render(request, "person.html", {"form": form})


def cities(request):
    data = json.loads(request.body)
    cities = Branch.objects.filter(country__id=data['user_id'])
    print(cities)
    return JsonResponse(list(cities.values("id", "name")), safe=False)


def display(request):
    return render(request, 'index.html')


def apply(request):
    return render(request, 'apply.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "USERNAME TAKEN")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                password=password)
                user.save()
            return redirect('login')
        else:
            messages.info(request, "NOT MATCHED")
            return redirect('register')

    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,
                                 password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'INVALID')
            return redirect('login')
        return redirect('home')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('login')