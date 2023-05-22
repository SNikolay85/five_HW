from django.urls import path

from measurement.views import SensorView, SensorUpdateView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
]
