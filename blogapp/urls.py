from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


# Define URL patterns for the application
urlpatterns = [
    path("", views.index, name="index"),
    path("article/<int:pk>/<slug:slug>", views.detail, name="detail"),
    path("register", views.signup, name="register"),
    path("accounts/login/", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
    path("profile_update", views.update_profile, name="update-profile"),
    path("profile", views.profile, name="profile"),
    path("view_profile/<int:pk>", views.view_user_profile, name="view-profile"),
    path("create", views.create_post, name="create"),
    path("update_post/<int:pk>", views.update_post, name="update-post"),
    path("delete_post/<int:pk>", views.delete_post, name="delete-post"),
]

# Define URL patterns related to authentication using Django's built-in views
auth_views_urlpatterns = {
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
}

# Combine the authentication-related URL patterns with the existing urlpatterns
urlpatterns += auth_views_urlpatterns

