from rest_framework.response import Response

from .models import Sensor, Measurement
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = SensorSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)

class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreateView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer_class = MeasurementSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)

