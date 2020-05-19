import json
from urllib.request import urlopen
from django.shortcuts import render, HttpResponse
# from .models import Product
import requests
import datetime
from datetime import timedelta


def index(request):
    # products = Product.objects.all()
    # return render(request, 'index.html', {'products': products})

    # querystring = {"format": "json"}
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
    headers = {
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
        'x-rapidapi-key': "fb3acd48b9mshbc47c3a4281bd66p105528jsncd3837fd509a"
    }

    response = requests.request(
        "GET", url, headers=headers)

    totalData = response.json()

    jsonUrl2 = "https://api.covid19india.org/data.json"
    stateData = json.load(urlopen(jsonUrl2))

    currentTime = datetime.datetime.now()

    all_data = {
        'stateData': stateData,
        'currentTime': currentTime,
        'totalData': totalData,
    }

    return render(request, 'index.html', all_data)


def distData(request):
    query = request.GET.get('state_name')

    jsonUrl = 'https://api.covid19india.org/v2/state_district_wise.json'
    distData = json.load(urlopen(jsonUrl))

    jsonUrl3 = "https://api.covid19india.org/zones.json"
    zonesData = json.load(urlopen(jsonUrl3))

    sub_data = {
        'distData': distData,
        'zonesData': zonesData,
        'query': query,
    }

    return render(request, 'dist.html', sub_data)
