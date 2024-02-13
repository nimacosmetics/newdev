from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginFom
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

def hompage(request):
    return render(request, "registration/index.html")

def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")
    context = {'register':form}
    return render(request, "registration/register.html", context=context)

def login_view(request):
    form = LoginFom()

    if request.method == "POST":
        form = LoginFom(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashbord")

    context = {"LoginForm":form}


    return render(request, "registration/my-login.html", context=context)



@login_required(login_url='login')
def dashbord(request):
    return render(request, "registration/dashbord.html")

def logout_view(request):

    auth.logout(request)
    return redirect("")
    
