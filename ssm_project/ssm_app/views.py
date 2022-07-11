from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from ssm_app.forms import CreateUserForm
from ssm_app.models import Song, Playlist
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(
        request,
        template_name='homepage.html')


def show_music_view(request):
    songs = Song.objects.all()

    return render(
        request,
        template_name='music.html',
        context={'songs': songs})


@login_required(login_url='login')
def show_blog_view(request):
    return render(
        request,
        template_name='blog.html')


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('/')


class PlaylistCreateView(CreateView):
    model = Playlist
    # form_class =
    # template_name =
    # success_url =


# Defining a register view:
def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('home'))
    else:
        register_form = CreateUserForm()

        if request.method == "POST":
            register_form = CreateUserForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                user = register_form.cleaned_data.get('username')
                messages.success(request, "Account was created for: " + user)
                return redirect(reverse_lazy('login'))
    return render(request, template_name="registration/register.html", context={"form": register_form})


# Defining a login view:
def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('home'))
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('home'))

            else:
                messages.info(request, "Username OR Password is incorrect! ")

    return render(request, template_name="registration/login.html", context={})


# Defining a logout view:
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('login'))


# class SignUpView(CreateView):
#     template_name = 'registration/register.html'
#     form_class = CreateUserForm
#     success_url = reverse_lazy('login')
#     model = User

# Defining a subscription plan view:
def subscribe_view(request):
    return render(request, template_name='subscription.html', context={})
