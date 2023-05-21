from rest_framework.response import Response

from .models import Sensor, Measurement
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

# CreateAPIView¶
# Используется только для создания конечных точек.
#create element class Sensor's (Предоставляет обработчик метода post.)
class SensorCreateView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


    def post(self, request, *args, **kwargs):
        name_sensor = request.GET.get('name')
        descr_sensor = request.GET.get('description')

        data = {
            'name': name_sensor,
            'description': descr_sensor
        }


        return Response(data)

# ListCreateAPIView¶
# Используется для конечных точек чтения-записи для представления коллекции экземпляров модели.
#create elements class Sensor's (Предоставляет обработчики методов get и post)
class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request, *args, **kwargs):
        return Response({'status': 'ok'})

class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request, *args, **kwargs):
        return Response({'status': 'ok'})

# RetrieveUpdateAPIView¶
# Используется для чтения или обновления конечных точек для представления одного экземпляра модели.
#
# Предоставляет обработчики методов get , put и patch.
class MeasurementUpdateView(RetrieveUpdateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer