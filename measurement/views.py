# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, SensorSerializer, MeasurementSerializer, SensorUpdateSerializer


# @api_view(['GET', 'POST'])
# def demo(request):
#     if request.method == 'GET':
#         sensors = Sensor.objects.all()
#         ser = SensorDetailSerializer(sensors, many=True)
#         return Response(ser.data)
#
#     if request.method == 'POST':
#         return Response({'status': 'oK'})


# class DemoView(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         ser = SensorDetailSerializer(sensors, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         return Response({'status': 'oK'})


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class UpdateSensor(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateSerializer