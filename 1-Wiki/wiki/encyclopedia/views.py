from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render, redirect

from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
            
def entries(request, title):

    entry = util.get_entry(title)

    if entry is None:
        return render(request, "encyclopedia/404.html")
    else:
        return render(request, "encyclopedia/entries.html", {
            "title": markdown2.markdown(entry),
            "titleTitle": title
            })

def entry_search(request):
    sub_list = []
    query = request.GET.get("q")
    entries = util.list_entries() 

    for entry in entries:
        if query.upper() == entry.upper():
            return redirect("entries", title = query)
        elif query.upper() in entry.upper():
                sub_list.append(entry)      
    return render(request, "encyclopedia/search.html", {
    "entries": sub_list,
    "search": True,
    "value": query
    })
    