from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .serializers import (
    UserSerializer,
    CleanseEntrySerializer,
    CleanseSerializer,
    RestrictionSerializer,
)
from .models import Cleanse, Restriction, CleanseEntry
from .forms import UserCreationForm, CleanseCreationForm, RestrictionCreationForm


class LandingPageView(APIView):
    def get(self, request, *args, **kwargs):
        # I dont like this way of getting the most recent cleanse
        cleanse = Cleanse.objects.last()
        cleanse_entries = CleanseEntry.objects.all()

        return render(
            request,
            "landing_page.html",
            {
                "cleanse": cleanse,
                "cleanse_entries": cleanse_entries,
            },
        )


class CreateUserAndDeleteView(CreateAPIView, DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, "create_user_form.html", {"form": form})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return redirect("home")

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CleanseCreateAndDeleteView(CreateAPIView, DestroyAPIView):
    queryset = Cleanse.objects.all()
    serializer_class = CleanseSerializer

    def get(self, request, *args, **kwargs):
        form = CleanseCreationForm()
        return render(request, "create_cleanse_form.html", {"form": form})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return redirect("home")

    def delete(self, request, *args, **kwargs):
        cleanse = self.get_object()
        cleanse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RestrictionCreateAndDeleteView(CreateAPIView, DestroyAPIView):
    queryset = Restriction.objects.all()
    serializer_class = RestrictionSerializer

    def get(self, request, *args, **kwargs):
        form = RestrictionCreationForm()
        return render(request, "create_restriction_form.html", {"form": form})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return redirect("home")

    def delete(self, request, *args, **kwargs):
        restriction = self.get_object()
        restriction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CleanseEntryCreateView(CreateAPIView):
    queryset = CleanseEntry.objects.all()
    serializer_class = CleanseEntrySerializer

    def get(self, request, *args, **kwargs):
        form = RestrictionCreationForm()
        return render(request, "create_entry_form.html", {"form": form})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return redirect("home")
