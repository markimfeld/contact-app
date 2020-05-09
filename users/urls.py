from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('edit-user', views.edit_user),
    path('password-change', views.password_change),
]