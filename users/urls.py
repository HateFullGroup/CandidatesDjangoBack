from django.contrib import admin
from django.urls import path, include
from users.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='create_user'),
]