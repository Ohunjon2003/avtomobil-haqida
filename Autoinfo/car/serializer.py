from .models import Marca
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser

class Marka:
    def __init__(self,name,info,price):
        self.name = name
        self.info = info
        self.price = price




class MarcaSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    info = serializers.CharField()
    price = serializers.DecimalField(max_digits=7,decimal_places=2)





def object_to_json():
    car = Marka('malibu','qora, avtomat',30000)
    serializer = MarcaSerializers(car)

    json = JSONRenderer().render(serializer.data)




def json_to_object():
    json = b'{"name":"malibu","info":"qora, avtomat","price":"30000.00"}'
    strem = io.BytesIO(json)
    data = JSONParser().parse(strem)
    serializer = MarcaSerializers(data=data)
    serializer.is_valid()

    car = Marca(**serializer.validated_data)




# class MarcaSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Marca
#         fields = '__all__'


