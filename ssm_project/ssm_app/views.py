from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from ssm_app.forms import CreateUserForm, PasswordChangingForm
from ssm_app.models import Song, Playlist, SubscriptionPlan
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required

import stripe
from django.views import View
from django.conf import settings
from django.views.generic import CreateView, ListView
from ssm_app.forms import PlaylistForm
from ssm_app.models import Song, Playlist


def homepage(request):
    return render(
        request,
        template_name='homepage.html')


def show_music_view(request):
    songs = Song.objects.all()
    playlist = Playlist.objects.all()

    return render(
        request,
        template_name='music.html',
        context={'songs': songs, 'playlists': playlist})


def show_blog_view(request):
    return render(
        request,
        template_name='blog.html')


class PlaylistCreateView(CreateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = 'playlist_create.html'
    success_url = reverse_lazy('playlist')

    def form_valid(self, form):
        valid = super().form_valid(form)
        if valid:
            playlist = form.save()
            playlist.user = self.request.user
            playlist.save()
        return valid


class PlaylistListView(ListView):
    model = Playlist
    context_object_name = 'all_playlists'
    template_name = 'playlist_list.html'


def add_song_to_playlist_view(request):
    if request.method == 'POST':
        playlist_id = request.POST['playlist_id']
        song_id = request.POST['song_id']
        song = Song.objects.get(id=song_id)
        playlist = Playlist.objects.get(id=playlist_id)
        song.playlists.add(playlist)
        song.save()

    return redirect(
        request.META['HTTP_REFERER'])  # Prin redirect, redirectionam userul catre locul unde a fost ultima oara


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
@login_required(login_url='login')
def subscribe_view(request):
    subscriptions = SubscriptionPlan.objects.all()

    return render(request, template_name='subscription.html', context={'subscriptions': subscriptions})


# Creating a session view for Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


# Creating a class to render the landing template view:

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        stripe_subscription_id = request.POST.get('stripe_subscription_id')
        YOUR_DOMAIN = "http://127.0.0.1:8000/"
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': stripe_subscription_id,
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=YOUR_DOMAIN + 'success/',
            cancel_url=YOUR_DOMAIN + 'cancel/',
        )
        return redirect(checkout_session.url, code=303)


# Creating a succcess html template view:
@login_required(login_url='login')
def success_view(request):
    return render(request, template_name="stripe_payments/success.html", context={})


# Creating a cancel html template view:
@login_required(login_url='login')
def cancel_view(request):
    return render(request, template_name="stripe_payments/cancel.html", context={})


# Creating a class for the change password functionality:
class PasswordsChangeView(PasswordChangeView):
    template_name = "registration/change_password.html"
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


# Creating a function view for the success_password_change:
def password_success(request):
    return render(request, template_name="registration/password_success.html", context={})
