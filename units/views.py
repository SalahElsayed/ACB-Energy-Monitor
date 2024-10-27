from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import ACBUnit, UnitConsumption
from .serializers import ACBUnitSerializer, UnitConsumptionSerializer
from rest_framework.decorators import action
from datetime import datetime


# ACB Unit Viewset 
class ACBUnitViewSet(viewsets.ModelViewSet):
    serializer_class = ACBUnitSerializer
    queryset = ACBUnit.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_fields = ['status']

    # Unit Consumption 
    @action(detail=True, methods=['get'])
    def consumption(self, request, pk=None):
        unit = self.get_object()  # get the object 
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)

        # get unit consumptions 
        unit_consumptions = UnitConsumption.objects.filter(unit=unit)

        # add filter with date 
        if start_date and end_date:
            start_date = datetime.fromisoformat(start_date)
            end_date = datetime.fromisoformat(end_date)
            unit_consumptions = unit_consumptions.filter(created_at__range=(start_date, end_date))

        serializer = UnitConsumptionSerializer(unit_consumptions, many=True)
        return Response(serializer.data)
