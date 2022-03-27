from django.shortcuts import render
from users.models import Owner, Pet
import json
from django.http import JsonResponse

context = {}

def homepage(request):
    context['listOfPets'] = Pet.objects.all()
    return render(request, 'dashboard/index.html', context)

def search_pet(request):
    pets = Pet.objects.all()
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')

        pets = Pet.objects.filter(name__icontains=search_str)

    data = pets.values()
    return JsonResponse(list(data), safe=False)

def pet_detail(request, pk):
    context['petDetail'] = Pet.objects.get(pk=pk)
    return render(request, 'dashboard/petdetail.html', context)