from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('contacts', views.list_contacts),
    path('contacts/create', views.create_contact),
    path('contacts/<int:pk>/delete', views.delete_contact),
    path('contacts/<int:pk>/edit', views.edit_contact),
]