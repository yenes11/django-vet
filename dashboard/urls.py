from unicodedata import name
from django.urls import path
from .views import homepage, search_pet, pet_detail
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', homepage, name='home'),
    path('search', csrf_exempt(search_pet), name='search'),
    path('pet/<int:pk>', pet_detail, name='pet-detail'),
]