from rest_framework import serializers
from .models import ACBUnit, UnitConsumption


# ACB Unit Serializer 
class ACBUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACBUnit
        fields = '__all__'


# ACB Unit Consumption Serializer 
class UnitConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitConsumption
        fields = '__all__'

    # to_represent unit 
    def to_representation(self, instance):
        response =  super().to_representation(instance)
        response['unit'] = ACBUnitSerializer(instance.unit).data 
        return response 