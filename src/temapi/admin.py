from django.contrib import admin

# Register your models here.
from .models import EntryDate, Discipline, Position
from .models import Employee, Client, Region, Site, DayRate
from .models import Rate, Equipment, EquipmentCharge, ManHoursCharge

admin.site.register(EntryDate)
admin.site.register(Discipline)
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Region)
admin.site.register(Site)
admin.site.register(Rate)
admin.site.register(DayRate)
admin.site.register(Equipment)
admin.site.register(EquipmentCharge)
admin.site.register(ManHoursCharge)