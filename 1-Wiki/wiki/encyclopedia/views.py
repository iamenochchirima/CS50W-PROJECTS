from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
import secrets

from . import util
import markdown2

class NewEntryForm(forms.Form):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={'class': 'form-control col-md-5 col-lg-3'})
        )
    content = forms.CharField(
        label="Entry markdown content",
        widget=forms.Textarea(attrs={'class': 'form-control col-md-8 col-lg-8'})
        )
    edit = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required=False)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, entry):

    entry_view = util.get_entry(entry)

    if entry_view is None:
        return render(request, "encyclopedia/404.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": entry,
            "entry": markdown2.markdown(entry_view)
            })

def entry_search(request):
    sub_list = []
    query = request.GET.get("q")
    entries = util.list_entries() 

    for entry in entries:
        if query.upper() == entry.upper():
            return redirect("entries", entry = query)
        elif query.upper() in entry.upper():
            sub_list.append(entry)      
    return render(request, "encyclopedia/search.html", {
        "entries": sub_list,
        "search": True,
        "value": query
        })

def create_entry(request):
    return render(request, "encyclopedia/create_entry.html", {
        "form": NewEntryForm()
    })

def new_entry(request):

    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():

            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if util.get_entry(title) is None or form.cleaned_data['edit'] is True:
                util.save_entry(title, content)
                return render(request, "encyclopedia/entry.html", {
            "entry": markdown2.markdown(content),
            "title": title
            })
            else:
                return render(request, "encyclopedia/new_entry_error.html")

def edit(request, entry):
    entry_view = util.get_entry(entry)
    
    form = NewEntryForm()
    form.fields['title'].initial = entry
    form.fields['content'].initial = entry_view
    form.fields['edit'].initial = True

    return render(request, "encyclopedia/create_entry.html", {
        "form": form,
        "edit": form.fields['edit'].initial,
        "title": form.fields['title'].initial
    })

def random(request):
    entries = util.list_entries()
    random_entry = secrets.choice(entries)
    return redirect("entries", entry = random_entry)