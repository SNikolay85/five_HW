from django.urls import path

from measurement.views import SensorView, MeasurementView, MeasurementUpdateView

urlpatterns = [
    path('measurement/sensors/', SensorView.as_view()),
    path('measurement/measurements/', MeasurementView.as_view()),
    path('measurement/sensors/<pk>', MeasurementUpdateView.as_view())
]
