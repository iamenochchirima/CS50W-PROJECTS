from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_entry", views.new_entry, name="new_entry"),
    path("entry_search", views.entry_search, name="entry_search"),
    path("create_entry", views.create_entry, name="create_entry"),
    path("random", views.random, name="random"),
    path("<str:entry>/edit", views.edit, name="edit"),
    path("<str:entry>", views.entries, name="entries")
]
