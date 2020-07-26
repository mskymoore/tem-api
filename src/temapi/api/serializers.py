from rest_framework import serializers
from temapi.models import Discipline, Position, Employee, Client
from temapi.models import Region, Site, Rate, Equipment, DayRate
from temapi.models import RateSheet, Worklog, EquipmentCharge
from temapi.models import ManHoursCharge, Dispute


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ('name',)


class PositionSerializer(serializers.ModelSerializer):
    discipline = serializers.SlugRelatedField(slug_field='name', queryset=Discipline.objects.all())
    class Meta:
        model = Position
        fields = ('name', 'discipline')


class EmployeeSerializer(serializers.ModelSerializer):
    position = serializers.SlugRelatedField(slug_field='name', queryset=Position.objects.all())
    discipline = serializers.SlugRelatedField(slug_field='name', queryset=Discipline.objects.all())
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
    region = serializers.SlugRelatedField(slug_field='name', queryset=Region.objects.all())
    class Meta:
        model = Site
        fields = (
            'name',
            'lat',
            'lon',
            'region',
        )


class RateSerializer(serializers.ModelSerializer):
    position = serializers.SlugRelatedField(slug_field='name', queryset=Position.objects.all())
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
    equipment = serializers.HyperlinkedRelatedField(
        view_name='equipment-detail', queryset=Equipment.objects.all())
    class Meta:
        model = DayRate
        fields = (
            'name',
            'cur_token',
            'cur_per_day',
            'equipment',
        )


class RateSheetSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(slug_field='name', queryset=Client.objects.all())
    region = serializers.SlugRelatedField(slug_field='name', queryset=Region.objects.all())
    day_rates = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='dayrate-detail'
    )
    rates = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='rate-detail'
    ) 
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
    client = serializers.SlugRelatedField(slug_field='name', queryset=Client.objects.all())
    site = serializers.SlugRelatedField(slug_field='name', queryset=Site.objects.all())
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
    equipment = serializers.HyperlinkedRelatedField(
        view_name='equipment-detail', queryset=Equipment.objects.all())
    worklog = serializers.HyperlinkedRelatedField(
        view_name='worklog-detail', queryset=Worklog.objects.all()
    )
    class Meta:
        model = EquipmentCharge
        fields = (
            'hours',
            'equipment',
            'worklog',
            'dispute',
            'date',
        )


class ManHoursChargeSerializer(serializers.ModelSerializer):
    employee = serializers.HyperlinkedRelatedField(
        view_name='employee-detail', queryset=Employee.objects.all())
    worklog = serializers.HyperlinkedRelatedField(
        view_name='worklog-detail', queryset=Worklog.objects.all()
    )
    dispute = serializers.HyperlinkedRelatedField(
        view_name='dispute-detail', queryset=Dispute.objects.all()
    )
    position = serializers.SlugRelatedField(slug_field='name', queryset=Position.objects.all())
    class Meta:
        model = ManHoursCharge
        fields = (
            'hours',
            'employee',
            'position',
            'worklog',
            'dispute',
            'date',
        )


class DisputeSerializer(serializers.ModelSerializer):
    worklog = serializers.HyperlinkedRelatedField(
        view_name='worklog-detail', queryset=Worklog.objects.all()
    ) 
    class Meta:
        model = Dispute
        fields = (
            'worklog',
            'summary', 
            'notes',
            'resolved'
        )