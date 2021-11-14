from .models import WeatherToday
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *



class WeatherDocumentSerializer(DocumentSerializer):
    class Meta:
        model = WeatherToday
        document = WeatherDocument
        fields = '__all__'