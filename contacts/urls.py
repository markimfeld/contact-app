from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('contacts', views.list_contacts),
    path('contacts/create', views.create_contact),
    path('contacts/delete/<int:id>', views.delete_contact),
]