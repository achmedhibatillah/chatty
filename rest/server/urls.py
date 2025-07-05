from django.urls import path, include
from .views import get_all, add, destroy

urlpatterns = [
    path('all', get_all),
    path('add', add),
    path('destroy', destroy)
]
