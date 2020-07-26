from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets, mixins
from temapi.models import Discipline, Position, Employee, Client
from temapi.models import Region, Site, Rate, Equipment, DayRate
from temapi.models import RateSheet, Worklog, Dispute, EquipmentCharge
from temapi.models import ManHoursCharge
from .serializers import DisciplineSerializer, PositionSerializer, EmployeeSerializer
from .serializers import ClientSerializer, RegionSerializer, SiteSerializer
from .serializers import RateSerializer, EquipmentSerializer, DayRateSerializer
from .serializers import RateSheetSerializer, WorklogSerializer, DisputeSerializer
from .serializers import EquipmentChargeSerializer, ManHoursChargeSerializer
from django.http import HttpResponse
import json


class CreateListUpdateRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):

    pass

class DisciplineViewSet(CreateListUpdateRetrieveViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

class PositionViewSet(CreateListUpdateRetrieveViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class EmployeeViewSet(CreateListUpdateRetrieveViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ClientViewSet(CreateListUpdateRetrieveViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class RegionViewSet(CreateListUpdateRetrieveViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class SiteViewSet(CreateListUpdateRetrieveViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class RateViewSet(CreateListUpdateRetrieveViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

class EquipmentViewSet(CreateListUpdateRetrieveViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class DayRateViewSet(CreateListUpdateRetrieveViewSet):
    queryset = DayRate.objects.all()
    serializer_class = DayRateSerializer

class RateSheetViewSet(CreateListUpdateRetrieveViewSet):
    queryset = RateSheet.objects.all()
    serializer_class = RateSheetSerializer

class WorklogViewSet(CreateListUpdateRetrieveViewSet):
    queryset = Worklog.objects.all()
    serializer_class = WorklogSerializer

class DisputeViewSet(CreateListUpdateRetrieveViewSet):
    queryset = Dispute.objects.all()
    serializer_class = DisputeSerializer

class EquipmentChargeViewSet(CreateListUpdateRetrieveViewSet):
    queryset = EquipmentCharge.objects.all()
    serializer_class = EquipmentChargeSerializer

class ManHoursChargeViewSet(CreateListUpdateRetrieveViewSet):
    queryset = ManHoursCharge.objects.all()
    serializer_class = ManHoursChargeSerializer
