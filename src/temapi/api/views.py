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


class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):

    pass

class DisciplineViewSet(CreateListRetrieveViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

class PositionViewSet(CreateListRetrieveViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class EmployeeViewSet(CreateListRetrieveViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ClientViewSet(CreateListRetrieveViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class RegionViewSet(CreateListRetrieveViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class SiteViewSet(CreateListRetrieveViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class RateViewSet(CreateListRetrieveViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

class EquipmentViewSet(CreateListRetrieveViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class DayRateViewSet(CreateListRetrieveViewSet):
    queryset = DayRate.objects.all()
    serializer_class = DayRateSerializer

class RateSheetViewSet(CreateListRetrieveViewSet):
    queryset = RateSheet.objects.all()
    serializer_class = RateSheetSerializer

class WorklogViewSet(CreateListRetrieveViewSet):
    queryset = Worklog.objects.all()
    serializer_class = WorklogSerializer

class DisputeViewSet(CreateListRetrieveViewSet):
    queryset = Dispute.objects.all()
    serializer_class = DisputeSerializer

class EquipmentChargeViewSet(CreateListRetrieveViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class ManHoursChargeViewSet(CreateListRetrieveViewSet):
    queryset = ManHoursCharge.objects.all()
    serializer_class = ManHoursChargeSerializer
