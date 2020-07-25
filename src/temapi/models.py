from django.db import models
from django.utils import timezone

class EntryDate(models.Model):
    date = models.DateField()


class Discipline(models.Model):
    name = models.CharField(max_length=256, null=False, default="discipline", unique=True)
    def __str__(self):
        return f"{self.name}"


class Position(models.Model):
    name = models.CharField(max_length=256, null=False, default="position", unique=True)
    discipline = models.ForeignKey(Discipline, related_name='discipline', on_delete=models.DO_NOTHING)
    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    number = models.PositiveIntegerField(null=False, default=0, unique=True)
    position = models.ForeignKey(Position, related_name='employees', on_delete=models.DO_NOTHING)
    discipline = models.ForeignKey(Discipline, related_name='employees', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=256, null=False, default="employee", unique=False)
    email = models.EmailField(max_length=256, null=False, default="employee@example.com", unique=True)
    def __str__(self):
        return f"{self.name}, {self.email}, {self.number}, {self.position}, {self.discipline}"


class Client(models.Model):
    name = models.CharField(max_length=256, null=False, default="client", unique=True)
    def __str__(self):
        return f"{self.name}"


class Region(models.Model):
    name = models.CharField(max_length=256, null=False, default=f"region", unique=True)
    clients = models.ManyToManyField(Client)
    def __str__(self):
        return f"{self.name}"


class Site(models.Model):
    name = models.CharField(max_length=256, null=False, default=f"site", unique=True)
    lat = models.FloatField(null=False, default=0)
    lon = models.FloatField(null=False, default=0)
    region = models.ForeignKey(Region, related_name='sites', on_delete=models.DO_NOTHING)
    clients = models.ManyToManyField(Client)
    def __str__(self):
        return f"{self.name} ({self.lat},{self.lon})"


class Rate(models.Model):
    name = models.CharField(max_length=256, null=True)
    cur_token = models.CharField(max_length=1, null=False, default="$")
    cur_per_hr = models.FloatField(null=False, default=0)
    ot_cur_per_hr = models.FloatField(null=False, default=0)
    client = models.ForeignKey(Client, related_name='rates', on_delete=models.DO_NOTHING)
    position = models.ForeignKey(Position, related_name='rates', on_delete=models.DO_NOTHING)
    region = models.ForeignKey(Region, related_name='rates', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.cur_token}{self.cur_per_hr}/hr for a {self.discipline} {self.position} for {self.client} in {self.region}"


class Equipment(models.Model):
    name = models.CharField(max_length=256, null=True)
    number = models.PositiveIntegerField(null=False, default=1, unique=True)

    def __str__(self):
        if self.name is not None:
            return f"{self.name}, {self.number}"
        else:
            return f"{self.number}"


class DayRate(models.Model):
    name = models.CharField(max_length=256, null=True)
    cur_token = models.CharField(max_length=1, null=False, default="$")
    cur_per_day = models.FloatField(null=False, default=0)
    equipment = models.ForeignKey(Equipment, related_name='day_rates', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Equipment: {self.equipment} at {self.cur_token}{self.cur_per_day}/day"


class RateSheet(models.Model):
    name = models.CharField(max_length=256, null=False)
    client = models.ForeignKey(Client, related_name='rate_sheets', on_delete=models.DO_NOTHING)
    region = models.ForeignKey(Region, related_name='rate_sheets', on_delet=models.DO_NOTHING)
    day_rates = models.ManyToManyField(DayRate)
    rates = models.ManyToManyField(Rate)

    def __str__(self):
        return f"{self.name} for {self.client} in {self.region} region"
    


class Worklog(model.Model):
    summary = models.CharField(max_length=32000, null=False)
    client = models.ForeignKey(Client, related_name='worklogs', on_delete=models.DO_NOTHING)
    site = models.ForeignKey(Site, related_name='worklogs', on_delete=models.DO_NOTHING)
    region = models.ForeignKey(Region, related_name='worklogs', on_delete=models.DO_NOTHING)
    approved = models.BooleanField(null=False, default=False)
    disputed = models.BooleanField(null=False, default=False)
    date = models.DateField()

    def __str__(self):
        return f"{self.date} - {self.client}, {self.site}, {self.region}"


class EquipmentCharge(models.Model):
    client = models.ForeignKey(Client, related_name='equipment_charges', on_delete=models.DO_NOTHING) 
    hours = models.PositiveIntegerField(null=False, default=0)
    equipment = models.ForeignKey(Equipment, related_name='charges', on_delete=models.DO_NOTHING)
    site = models.ForeignKey(Site, related_name='equipment_charges', on_delete=models.DO_NOTHING)
    worklog = models.ForeignKey(Worklog, related_name='equipment_charges', on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return f"{self.hours}hrs of {self.equipment} at {self.site} for {self.client}"


class ManHoursCharge(models.Model):
    client = models.ForeignKey(Client, related_name='manhours_charges', on_delete=models.DO_NOTHING)
    site = models.ForeignKey(Site, related_name='manhours_charges', on_delete=models.DO_NOTHING)
    hours = models.PositiveIntegerField(null=False, default=0)
    employee = models.ForeignKey(Employee, related_name='charges', on_delete=models.DO_NOTHING)
    position = models.ForeignKey(Position, related_name='charges', on_delete=models.DO_NOTHING)
    worklog = models.ForeignKey(Worklog, related_name='manhours_charges')
    date = models.DateField()

    def __str__(self):
        return f"{self.hours}hrs worked by {self.employee} at {self.site} for {self.client}"


class Dispute(models.Model):
    worklog = models.ForeignKey(Worklog, related_name='disputes', on_delete=models.DO_NOTHING)
    summary = models.CharField(max_length=1008, null=False)
    notes = models.CharField(max_length=32000, null=True)
    equipment_charges = models.ManyToManyField(EquipmentCharge)
    manhours_charges = models.ManyToManyField(ManHoursCharge)


