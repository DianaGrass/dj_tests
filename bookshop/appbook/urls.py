from django.urls import path
from appbook import views

urlpatterns = [
    path("", views.hello),
    path("world", views.world),
]