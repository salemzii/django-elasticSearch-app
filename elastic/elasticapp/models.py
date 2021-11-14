from django.db import models
from django.utils import timezone


class WeatherToday(models.Model):
    city = models.CharField(max_length=20)
    temperature = models.FloatField()
    description = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        template = f"{self.city} on {self.date.date()}"
        return template.format(self)


