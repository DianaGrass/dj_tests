from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    # return HttpResponse("hello!")

    # return render(request, "index.html", {"name": "Egor", "title": "hodor"})

    response = {"name": "Egor", "title": "hodor", "user": "Oleg"}
    return render(request, "index.html", response)



def world(request):
    response = {"name": "-Egor", "title": "new", "user": "-Oleg"}
    return render(request, "newindex.html", response)

