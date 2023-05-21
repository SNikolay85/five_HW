from django.urls import path

from measurement.views import SensoreView, MeasurementView

urlpatterns = [
    path('measurement/sensor/', SensoreView.as_view()),
    path('measurement/measure/', MeasurementView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
