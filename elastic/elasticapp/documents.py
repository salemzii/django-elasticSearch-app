from django_elasticsearch_dsl import(
    Document, fields, Index
)
from .models import WeatherToday



PUBLISHER_INDEX = Index('elastic')

PUBLISHER_INDEX.settings(
    number_of_shards = 1,
    number_of_replicas = 1
)


@PUBLISHER_INDEX.doc_type
class WeatherDocument(Document):
    id = fields.IntegerField(attr="id")

    title = fields.TextField(
        fields = {
            "raw": {
                "type": "keyword"
            }
        }
    )
    temperature = fields.FloatField()
    description = fields.TextField(
        fields = {
            "raw": {
                "type": "keyword"
            }
        }
    )    

    date = fields.DateField()

    class Django:
        model = WeatherToday


