from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temp_measure = models.FloatField()
    time_measure = models.DateTimeField(auto_now_add=True)
    image = models.URLField(null=True, blank=True)

