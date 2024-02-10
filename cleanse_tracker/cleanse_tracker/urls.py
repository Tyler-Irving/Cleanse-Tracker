"""
URL configuration for cleanse_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app.views import (
    CreateUserAndDeleteView,
    LandingPageView,
    CleanseCreateAndDeleteView,
    CleanseEntryCreateView,
    RestrictionCreateAndDeleteView,
)

urlpatterns = [
    path("", LandingPageView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("create_user/", CreateUserAndDeleteView.as_view(), name="create_user"),
    path(
        "delete_user/<int:pk>/", CreateUserAndDeleteView.as_view(), name="delete_user"
    ),
    path(
        "create_cleanse/", CleanseCreateAndDeleteView.as_view(), name="create_cleanse"
    ),
    path(
        "delete_cleanse/<int:pk>/",
        CleanseCreateAndDeleteView.as_view(),
        name="delete_cleanse",
    ),
    path(
        "create_restriction/",
        RestrictionCreateAndDeleteView.as_view(),
        name="create_restriction",
    ),
    path(
        "delete_restriction/<int:pk>/",
        RestrictionCreateAndDeleteView.as_view(),
        name="delete_restriction",
    ),
    path("create_entry/", CleanseEntryCreateView.as_view(), name="create_entry"),
]
