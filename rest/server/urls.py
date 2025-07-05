from django.urls import path, include
from .views import get_all, get_detail, add, destroy

urlpatterns = [
    path('all', get_all),
    path('detail/<code>', get_detail),
    path('add', add),
    path('destroy', destroy),
]
