from django.forms import model_to_dict
from django.shortcuts import render
from .models import Marca,Brand
from rest_framework.generics import ListAPIView,RetrieveAPIView
# Create your views here.
from .serializer import MarcaSerializers
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
class MarcaList(APIView):
    def get(self,request:Request):
        cars = Marca.objects.values()
        return Response({'cars':list(cars)})

    def post(self,request:Request):
        car = Marca.objects.create(
            name = request.data['name'],
            price = request.data['price'],
            brand_id = request.data['brand_id']
        )
        return Response({"car":model_to_dict(car),'message': "car qoshildi"})






# class MarcaList(ListAPIView):
#     queryset = Marca.objects.all()
#     serializer_class = MarcaSerializers
#
#
# class MarcaDetail(RetrieveAPIView):
#     queryset = Marca.objects.all()
#     serializer_class = MarcaSerializers

