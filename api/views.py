from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
import permissions as api_permissions
from api.serializers import Test1Serializer, Test2Serializer, Test3Serializer, BookreadSerializer, UserSerializer, \
    BookshareSerializer
from authuser.models import Test1, Test2, Test3, MyUser
from book.models import Article


class Test1ViewSet(viewsets.ModelViewSet):
    queryset = Test1.objects.all()
    serializer_class = Test1Serializer
class Test2ViewSet(viewsets.ModelViewSet):
    queryset = Test2.objects.all()
    serializer_class = Test2Serializer
class Test3ViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,
                          )
    queryset = Test3.objects.all()
    serializer_class = Test3Serializer
class BookReadViewSet(viewsets.ModelViewSet):
    permissions=(permissions.IsAuthenticated,api_permissions.IsOwnerOrReadOnly)
    queryset = Article.objects.filter(type=0)
    serializer_class = BookreadSerializer
class BookShareViewSet(viewsets.ModelViewSet):
    permissions=(permissions.IsAuthenticated,api_permissions.IsOwnerOrReadOnly)
    queryset = Article.objects.filter(type=1)
    serializer_class = BookshareSerializer

class UserViewSet(viewsets.ModelViewSet):
    permissions = (permissions.IsAuthenticated, api_permissions.IsOwnerOrReadOnly)
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer