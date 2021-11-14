from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from .models import WeatherToday
import random
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import *
from .serializers import *
from django_elasticsearch_dsl_drf.filter_backends import(
    FilteringFilterBackend,
    CompoundSearchFilterBackend,  
)


def get_data():
    cities = ['kano', 'lagos', 'dutse', 'benin', 'london', 'oslo', 'moscow', 'new delhi', 'toronto'
    'accra', 'nairobi'
    ]
    api_key = '96339800e17c3282962f96779da19cf3'

    for city in random.sample(cities, 5):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        r= requests.get(url)
        payload = json.loads(r.text)
        WeatherToday.objects.create(
            city= city,
            description= payload['weather'][0]['description'],
            temperature= payload['main']['temp']
        )
        



def view_response(request):
    get_data()
    return JsonResponse({'status': 200})



class PublisherDocumentView(DocumentViewSet):
    document = WeatherDocument
    serializer_class = WeatherDocumentSerializer


    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend,
    ]


    search_fields =  ('title', 'description')
    multi_match_search_fields = ('title', 'description')
    filter_fields = {
        'title': 'title',
        'description': 'description'
    }



