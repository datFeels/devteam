from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('saving')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('admin-page')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    # if POST gets called
    if request.method == "POST":
        # get username and password from POST
        username = request.POST.get("username")
        password = request.POST.get("password")
        # using authenticate function to check username and password
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                "error": "invalid username or password"
            }
            return render(request, "users/login.html", context)
        # actually log in the user
        login(request, user)
        # redirect to homepage
        return redirect("course-list")
    # renders login page when called
    return render(request, "users/login.html", {})


def logout_view(request):
    # if POST gets called
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return render(request, "users/logout.html", {})
