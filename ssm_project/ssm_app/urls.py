from django.urls import path

from ssm_app.views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('music/', show_music_view, name='music'),
    path('blog/', show_blog_view, name='blog'),
    # CHANGE PASSWORD
    path('password-change/', MyPasswordChangeView.as_view(), name='password_change'),
    # SUBSCRIPTION
    path('subscription/', subscribe_view, name='subscribe'),
    # REGISTRATION
    path('register/', register_view, name='register'),
    # LOGIN
    path('login/', login_view, name='login'),
    # LOGOUT
    path('logout/', logout_view, name='logout'),

    # Checkout session Stripe:
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),

    # path('subscription/', show_subscription_view, name="subscription"),

    # CREATE LIBRARY
    path('create-playlist/', PlaylistCreateView.as_view(), name='playlist_create'),
    # LIBRARY
    path('playlist-list/', PlaylistListView.as_view(), name='playlist'),
    path('add-song-to-playlist/', add_song_to_playlist_view, name='add_song_to_playlist'),
    path('success/', success_view, name='success'),
    path('cancel/', cancel_view, name='cancel'),
]
