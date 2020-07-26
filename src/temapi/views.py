from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets, mixins
from temapi.models import Discipline, Position, Employee, Client
from temapi.models import Region, Site, Rate, Equipment, DayRate
from temapi.models import RateSheet, Worklog, Dispute, EquipmentCharge
from temapi.models import ManHoursCharge
from temapi.serializers import DisciplineSerializer, PositionSerializer, EmployeeSerializer
from temapi.serializers import ClientSerializer, RegionSerializer, SiteSerializer
from temapi.serializers import RateSerializer, EquipmentSerializer, DayRateSerializer
from temapi.serializers import RateSheetSerializer, WorklogSerializer, DisputeSerializer
from temapi.serializers import EquipmentChargeSerializer, ManHoursChargeSerializer
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse as Response
from django.contrib import messages
from djreact.settings import PROTOCOL, HOSTNAME, PORT
# from djoser import views
import requests

# see https://djoser.readthedocs.io/en/latest/examples.html


def reset_user_password(request, uid, token):
    if request.POST:
        password = request.POST.get('the_new_password')
        confirmed_password = request.POST.get('confirmed_password')

        if password != confirmed_password:
            context = {'failed': True}
            return render(request, 'reset_password.html', context)

        payload = {'uid': uid, 'token': token, 'new_password': password}

        url = f"{PROTOCOL}://{HOSTNAME}{PORT}/auth/users/reset_password_confirm/"

        response = requests.post(url, data=payload)
        if response.status_code == 204:
            messages.success(
                request, 'Your password has been reset successfully!')
            context = {'success': True}
            return render(request, 'password_reset_result.html', context)
        else:
            context = {'success': False}
            return render(request, 'password_reset_result.html', context)
    else:
        context = {'failed': False}
        return render(request, 'reset_password.html', context)


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
