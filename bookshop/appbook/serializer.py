from rest_framework.serializers import ModelSerializer
from appbook.models import Book
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name")



class BookSerializer(ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Book
        fields = "__all__"


class BookSerializerCreate(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
