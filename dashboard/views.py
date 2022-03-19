from django.shortcuts import render
from users.models import Owner, Pet

def homepage(request):
    context = {
        'listOfPets' : Pet.objects.all()
    }
    return render(request, 'dashboard/index.html', context)