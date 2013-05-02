from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from places.models import Place
import json

def index(request):
    latest_place_list = Place.objects.order_by('-pub_date')[:5]
    context = {'latest_place_list': latest_place_list}
    return render(request, 'places/index.html', context)
    #data = [Place.name]
    #return HttpResponse(json.dumps(data), content_type'places/json')

def detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return render(request, 'places/detail.html', {'place': place})
