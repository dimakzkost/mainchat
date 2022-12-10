from django.contrib import auth
from django.shortcuts import render
from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'