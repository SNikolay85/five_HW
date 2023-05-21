from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='mesurements')
    temp_measure = models.FloatField()
    time_measure = models.TimeField(auto_now=False, auto_now_add=False)

