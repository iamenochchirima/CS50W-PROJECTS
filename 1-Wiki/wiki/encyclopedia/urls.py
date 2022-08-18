from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entry_search", views.entry_search, name="entry_search"),
    path("<str:title>", views.entries, name="entries")
]
