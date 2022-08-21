from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entry_search", views.entry_search, name="entry_search"),
    path("create_entry", views.create_entry, name="create_entry"),
    path("<str:title>/edit", views.entries, name="edit"),
    path("new_entry", views.new_entry, name="new_entry"),
    path("<str:title>", views.entries, name="entries")
]
