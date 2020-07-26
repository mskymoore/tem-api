from rest_framework import serializers
from temapi.models import Discipline, Position, Employee, Client
from temapi.models import Region, Site, Rate, Equipment, DayRate
from temapi.models import RateSheet, Worklog, EquipmentCharge
from temapi.models import ManHoursCharge, Dispute, User
from djoser.serializers import UserCreateSerializer, UserSerializer
from djoser.conf import settings
from django.contrib.auth import authenticate


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password',
                  'first_name', 'last_name', 'phone')


class TokenCreateSerializer(serializers.Serializer):
    password = serializers.CharField(
        required=False, style={"input_type": "password"})

    default_error_messages = {
        "invalid_credentials": settings.CONSTANTS.messages.INVALID_CREDENTIALS_ERROR,
        "inactive_account": settings.CONSTANTS.messages.INACTIVE_ACCOUNT_ERROR,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields[settings.LOGIN_FIELD] = serializers.CharField(
            required=False)

    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(request=self.context.get(
            "request"), **params, password=password)
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        if self.user and self.user.is_active:
            return attrs
        self.fail("invalid_credentials")


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ('url', 'name',)


class PositionSerializer(serializers.ModelSerializer):
    discipline = serializers.SlugRelatedField(
        slug_field='name', queryset=Discipline.objects.all())

    class Meta:
        model = Position
        fields = ('url', 'name', 'discipline')


class EmployeeSerializer(serializers.ModelSerializer):
    position = serializers.SlugRelatedField(
        slug_field='name', queryset=Position.objects.all())
    discipline = serializers.SlugRelatedField(
        slug_field='name', queryset=Discipline.objects.all())

    class Meta:
        model = Employee
        fields = (
            'url',
            'number',
            'position',
            'discipline',
            'name',
            'email'
        )


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('url', 'name',)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('url', 'name',)


class SiteSerializer(serializers.ModelSerializer):
    region = serializers.SlugRelatedField(
        slug_field='name', queryset=Region.objects.all())

    class Meta:
        model = Site
        fields = (
            'url',
            'name',
            'lat',
            'lon',
            'region',
        )


class RateSerializer(serializers.ModelSerializer):
    position = serializers.SlugRelatedField(
        slug_field='name', queryset=Position.objects.all())

    class Meta:
        model = Rate
        fields = (
            'url',
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
            'url',
            'name',
            'number',
        )


class DayRateSerializer(serializers.ModelSerializer):
    equipment = serializers.HyperlinkedRelatedField(
        view_name='equipment-detail', queryset=Equipment.objects.all())

    class Meta:
        model = DayRate
        fields = (
            'url',
            'name',
            'cur_token',
            'cur_per_day',
            'equipment',
        )


class RateSheetSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(
        slug_field='name', queryset=Client.objects.all())
    region = serializers.SlugRelatedField(
        slug_field='name', queryset=Region.objects.all())
    day_rates = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='dayrate-detail',
        queryset=DayRate.objects.all()
    )
    rates = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='rate-detail',
        queryset=Rate.objects.all()
    )

    class Meta:
        model = RateSheet
        fields = (
            'url',
            'name',
            'client',
            'region',
            'day_rates',
            'rates',
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
            'url',
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
    position = serializers.SlugRelatedField(
        slug_field='name', queryset=Position.objects.all())

    class Meta:
        model = ManHoursCharge
        fields = (
            'url',
            'hours',
            'employee',
            'position',
            'worklog',
            'dispute',
            'date',
        )


class WorklogSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(
        slug_field='name', queryset=Client.objects.all())
    site = serializers.SlugRelatedField(
        slug_field='name', queryset=Site.objects.all())
    manhours_charges = ManHoursChargeSerializer(many=True)
    equipment_charges = EquipmentChargeSerializer(many=True)

    class Meta:
        model = Worklog
        fields = (
            'url',
            'summary',
            'client',
            'site',
            'approved',
            'disputed',
            'manhours_charges',
            'equipment_charges',
            'date',
        )


class DisputeSerializer(serializers.ModelSerializer):
    worklog = serializers.HyperlinkedRelatedField(
        view_name='worklog-detail', queryset=Worklog.objects.all()
    )
    manhours_charges = ManHoursChargeSerializer(many=True)
    equipment_charges = EquipmentChargeSerializer(many=True)

    class Meta:
        model = Dispute
        fields = (
            'url',
            'worklog',
            'summary',
            'notes',
            'resolved',
            'manhours_charges',
            'equipment_charges',
        )
