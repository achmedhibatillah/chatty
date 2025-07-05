from django.urls import path, include
from .views import message

urlpatterns = [
    path('ask', message),
]