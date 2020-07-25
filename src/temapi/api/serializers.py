from rest_framework import serializers
from temapi.models import EntryDate
from temapi.models import Discipline, Position, Employee, Client
from temapi.models import Region, Site, Rate, Equipment, DayRate
from temapi.models import RateSheet, Worklog, EquipmentCharge
from temapi.models import ManHoursCharge, Dispute

class EntryDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryDate
        fields = ('date',)


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ('name',)


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('name', 'discipline')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'number',
            'position',
            'discipline',
            'name',
            'email'
        )


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name',)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('name',)


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = (
            'name',
            'lat',
            'lon',
            'region',
        )


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'name',
            'cur_token',
            'cur_per_hr',
            'ot_cur_per_hr',
            'position',
        )


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = (
            'name',
            'number',
        )


class DayRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayRate
        fields = (
            'name',
            'cur_token',
            'cur_per_day',
            'equipment',
        )


class RateSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateSheet
        fields = (
            'name',
            'client',
            'region',
            'day_rates',
            'rates',
        )


class WorklogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worklog
        fields = (
            'summary',
            'client',
            'site',
            'approved',
            'disputed',
            'date',
        )


class EquipmentChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentCharge
        fields = (
            'hours',
            'equipment',
            'worklog',
            'date',
        )


class ManHoursChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManHoursCharge
        fields = (
            'hours',
            'employee',
            'position',
            'worklog',
            'date',
        )


class DisputeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispute
        fields = (
            'worklog',
            'summary', 
            'notes',
            'equipment_charges',
            'manhours_charges',
        )