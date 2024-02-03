from django.urls import path
from .views import property_list
from .views import property_search

urlpatterns = [
    path('templates/', property_list),
    path('templates/', property_search),
]
