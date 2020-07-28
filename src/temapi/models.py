from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from temapi.const import manager_role_id, client_role_id, employee_role_id


class Client(models.Model):
    name = models.CharField(max_length=256, null=False,
                            default="client", unique=True)

    def __str__(self):
        return f"{self.name}"


class Discipline(models.Model):
    name = models.CharField(max_length=256, null=False,
                            default="discipline", unique=True)

    def __str__(self):
        return f"{self.name}"


class Position(models.Model):
    name = models.CharField(max_length=256, null=False,
                            default="", unique=True)
    discipline = models.ForeignKey(
        Discipline, related_name='discipline', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    number = models.PositiveIntegerField(null=False, default=0, unique=True)
    position = models.ForeignKey(
        Position, related_name='employees', on_delete=models.DO_NOTHING)
    discipline = models.ForeignKey(
        Discipline, related_name='employees', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.number}, {self.position}, {self.discipline}"


class User(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              null=False, max_length=256, unique=True)
    phone = models.CharField(null=False, max_length=256, unique=True)

    # this is how we determine worklog view permissions, and ability to dispute worklogs
    client = models.ForeignKey(
        Client, related_name='users', on_delete=models.CASCADE, null=True, blank=True)

    # this is how we determine ability to submit worklogs, and resolve disputes
    employee = models.ForeignKey(
        Employee, related_name='users', on_delete=models.CASCADE, null=True, blank=True)

    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name']

    USERNAME_FIELD = 'email'

    MANAGER = manager_role_id
    CLIENT = client_role_id
    EMPLOYEE = employee_role_id

    # this is how we determine templates and views to render
    ROLE_CHOICES = (
        (MANAGER, 'Manager'),
        (CLIENT, 'Client'),
        (EMPLOYEE, 'Employee')
    )

    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True)

    def get_username(self):
        return self.email


class Region(models.Model):
    name = models.CharField(max_length=256, null=False,
                            default=f"region", unique=True)
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return f"{self.name}"


class Site(models.Model):
    name = models.CharField(max_length=256, null=False,
                            default=f"site", unique=True)
    lat = models.FloatField(null=False, default=0)
    lon = models.FloatField(null=False, default=0)
    region = models.ForeignKey(
        Region, related_name='sites', on_delete=models.DO_NOTHING)
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return f"{self.name} ({self.lat},{self.lon})"


class Rate(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    cur_token = models.CharField(max_length=1, null=False, default="$")
    cur_per_hr = models.FloatField(null=False, default=0)
    ot_cur_per_hr = models.FloatField(null=False, default=0)
    position = models.ForeignKey(
        Position, related_name='rates', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.cur_token}{self.cur_per_hr}/hr for a {self.position}"


class Equipment(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    number = models.PositiveIntegerField(null=False, default=1, unique=True)

    def __str__(self):
        if self.name is not None:
            return f"{self.name}, {self.number}"
        else:
            return f"{self.number}"


class DayRate(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    cur_token = models.CharField(max_length=1, null=False, default="$")
    cur_per_day = models.FloatField(null=False, default=0)
    equipment = models.ForeignKey(
        Equipment, related_name='day_rates', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.equipment} at {self.cur_token}{self.cur_per_day}/day"


class RateSheet(models.Model):
    name = models.CharField(max_length=256, null=False)
    client = models.ForeignKey(
        Client, related_name='rate_sheets', on_delete=models.DO_NOTHING)
    region = models.ForeignKey(
        Region, related_name='rate_sheets', on_delete=models.DO_NOTHING)
    day_rates = models.ManyToManyField(DayRate)
    rates = models.ManyToManyField(Rate)

    def __str__(self):
        return f"{self.name} for {self.client} in {self.region} region"

# TODO: add context to these models such that booleans etch
# begin with a clause like is, am, was, are, were, had.   example: is_approved, is_disputed


class Worklog(models.Model):
    # TODO: Track creator, editors, and edits
    created_by = models.ForeignKey(
        User, related_name='created_worklogs', on_delete=models.DO_NOTHING, null=False, blank=False)
    included_employees = models.ManyToManyField(Employee)
    summary = models.CharField(max_length=32000, null=False)
    client = models.ForeignKey(
        Client, related_name='worklogs', on_delete=models.DO_NOTHING)
    site = models.ForeignKey(
        Site, related_name='worklogs', on_delete=models.DO_NOTHING)
    approved = models.BooleanField(null=False, default=False)
    disputed = models.BooleanField(null=False, default=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.date} - {self.client}, {self.site}"


class Dispute(models.Model):
    created_by = models.ForeignKey(
        User, related_name='created_disputes', on_delete=models.DO_NOTHING, null=False, blank=False)
    worklog = models.ForeignKey(
        Worklog, related_name='disputes', on_delete=models.DO_NOTHING)
    summary = models.CharField(max_length=1008, null=False)
    notes = models.CharField(max_length=32000, null=True, blank=True)
    resolved = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f"{self.summary} - {self.worklog}"


class EquipmentCharge(models.Model):
    created_by = models.ForeignKey(
        User, related_name='created_equipment_charges', on_delete=models.DO_NOTHING, null=False, blank=False)
    hours = models.FloatField(null=False, default=0)
    equipment = models.ForeignKey(
        Equipment, related_name='charges', on_delete=models.DO_NOTHING)
    worklog = models.ForeignKey(
        Worklog, related_name='equipment_charges', on_delete=models.DO_NOTHING)
    dispute = models.ForeignKey(
        Dispute, related_name='equipment_charges', on_delete=models.DO_NOTHING, null=True, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.hours} hours of {self.equipment}"


class ManHoursCharge(models.Model):
    created_by = models.ForeignKey(
        User, related_name='created_manhrs_charges', on_delete=models.DO_NOTHING, null=False, blank=False)
    hours = models.FloatField(null=False, default=0)
    employee = models.ForeignKey(
        Employee, related_name='charges', on_delete=models.DO_NOTHING)
    position = models.ForeignKey(
        Position, related_name='charges', on_delete=models.DO_NOTHING)
    worklog = models.ForeignKey(
        Worklog, related_name='manhours_charges', on_delete=models.DO_NOTHING)
    dispute = models.ForeignKey(
        Dispute, related_name='manhours_charges', on_delete=models.DO_NOTHING, null=True, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.hours} hours worked by {self.employee}"
