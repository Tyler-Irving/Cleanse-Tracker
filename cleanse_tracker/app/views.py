from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import (
    UserSerializer,
    CleanseEntrySerializer,
    CleanseSerializer,
    RestrictionSerializer,
)
from .models import Cleanse, Restriction, CleanseEntry


class CreateUserAndDeleteView(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CleanseCreateAndDeleteView(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = Cleanse.objects.all()
    serializer_class = CleanseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def delete(self, request, *args, **kwargs):
        cleanse = self.get_object()
        cleanse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RestrictionCreateAndDeleteView(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = Restriction.objects.all()
    serializer_class = RestrictionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def delete(self, request, *args, **kwargs):
        restriction = self.get_object()
        restriction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CleanseCreateView(generics.CreateAPIView):
    queryset = CleanseEntry.objects.all()
    serializer_class = CleanseEntrySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
