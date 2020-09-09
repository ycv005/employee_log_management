from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import UserSerializer, GlobalUserSerializer
from django.contrib.auth import get_user_model
from .models import GlobalUser
from rest_framework import filters
from itertools import chain


class UserList(generics.ListCreateAPIView):
    """View and create user"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """View user's detail"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GlobalUserList(generics.ListCreateAPIView):
    """View and create user"""
    serializer_class = GlobalUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = GlobalUser.objects.all()
        q = self.request.query_params.get('search', None)
        if q:
            q = q.strip()
            if q.isdigit() or q[1:].isdigit():
                if q[0] != '+' and len(q) == 12:
                    q = '+' + q
                if len(q) < 13:
                    queryset = GlobalUser.objects.filter(
                        phone_number__contains=q)
                else:
                    queryset = GlobalUser.objects.filter(phone_number=q)
                    if len(queryset) > 1:
                        pass
                    queryset = GlobalUser.objects.filter(
                        phone_number__contains=q)
            elif q.isalpha():
                pre_query = GlobalUser.objects.filter(names__name=q)
                post_query = GlobalUser.objects.filter(
                    names__name__contains=q).exclude(names__name=q)
                queryset = list(chain(pre_query, post_query))
        return queryset


class GlobalUserDetail(generics.RetrieveUpdateDestroyAPIView):
    """View user's detail"""
    queryset = GlobalUser.objects.all()
    serializer_class = GlobalUserSerializer
    permission_classes = [permissions.IsAuthenticated]
