from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

execfile(r"tripbuilder\booker.py")

import unirest

def search(request):
    """
    Search page for hotel search
    """
    return render(request, "tripbuilder/search.html", {})

def results(request):
    """
    Results display view for hotel search
    """
    names = searchHotels(request.POST['location'])
    context = {'names': names}
    return render(request, "tripbuilder/results.html", context)

