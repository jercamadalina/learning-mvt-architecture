from django.urls import path

from ssm_app.views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', homepage, name='home'),
    path('blog/', show_blog_view, name='blog'),
    path('music/', show_music_view, name='music'),
    path('your-library/', YourLibraryView.as_view(), name='your-library'),
    path('create-playlist/', PlaylistCreateView.as_view(), name='playlist_create'),
    path('subscription/', subscribe_view, name='subscribe'),
    path('add-song-to-playlist/', add_song_to_playlist_view, name='add_song_to_playlist'),
    path('your_playlist/<int:pk>/', your_playlist, name='your_playlist'),
    path('delete/<int:id>/', delete_song_from_playlist, name='delete'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('password_success/', password_success, name='password_success'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='reset_password'),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-change/', PasswordsChangeView.as_view(), name='change_password'),
    # path('password-change/', PasswordChangeView.as_view(), name='password_change'),

    # PASSWORD RESET CONFIRM (Link in email)
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # PASSWORD RESET COMPLETE (Success message)
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # Checkout session Stripe:
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),

    # Stripe payments
    path('success/', success_view, name='success'),
    path('cancel/', cancel_view, name='cancel'),
]
