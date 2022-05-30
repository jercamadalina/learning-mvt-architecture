from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from ssm_app.models import Song


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
