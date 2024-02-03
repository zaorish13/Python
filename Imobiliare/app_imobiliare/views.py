from django.db.models import Q
from django.shortcuts import render
from .models import RealEstate


def property_list(request):
    properties = RealEstate.objects.all()
    return render(request, 'property_list.html', {'properties': properties})


def property_search(request):
    rezultat = request.GET.get('search', '')
    properties = RealEstate.objects.all()

    if rezultat:
        properties = properties.filter(
            Q(RS_titlu__icontains=rezultat) |
            Q(RS_zona__icontains=rezultat) |
            Q(RS_compartimentare__icontains=rezultat) |
            Q(RS_stare_proprietate__icontains=rezultat) |
            Q(RS_descriere__icontains=rezultat) |
            Q(RS_pret__icontains=rezultat)
        )

    return render(request, "property_list.html", {'properties': properties})
