from django.shortcuts import render
from django.http import HttpResponse
from appbook.serializer import BookSerializer, BookSerializerCreate
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from appbook.models import Book

# Create your views here.

def hello(request):
    # return HttpResponse("hello!")
    # return render(request, "index.html", {"name": "Egor", "title": "hodor"})
    response = {"name": "Egor", "title": "hodor", "user": "Oleg"}
    return render(request, "index.html", response)


def world(request):
    response = {"name": "-Egor", "title": "new", "user": "-Oleg"}
    return render(request, "newindex.html", response)


class BookListView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookCreateView(CreateAPIView):
    serializer_class = BookSerializerCreate

class BookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializerCreate
    queryset = Book.objects.all()

