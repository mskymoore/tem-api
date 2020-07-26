from django.contrib import admin

# Register your models here.
from .models import EntryDate, Discipline, Position
from .models import Employee, Client, Region, Site, DayRate
from .models import Rate, Equipment, EquipmentCharge, ManHoursCharge
from .models import Worklog, Dispute, RateSheet


class ManHoursChargeAdminTab(admin.TabularInline):
    model = ManHoursCharge

class EquipmentChargeAdminTab(admin.TabularInline):
    model = EquipmentCharge

class PositionAdminTab(admin.TabularInline):
    model = Position

class WorklogAdminTab(admin.TabularInline):
    model = Worklog

class WorklogAdmin(admin.ModelAdmin):
   inlines = [ManHoursChargeAdminTab, EquipmentChargeAdminTab]

class EquipmentAdmin(admin.ModelAdmin):
    inlines = [EquipmentChargeAdminTab,]

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [ManHoursChargeAdminTab,]

class PositionAdmin(admin.ModelAdmin):
    inlines = [ManHoursChargeAdminTab,]

class ClientAdmin(admin.ModelAdmin):
    inlines = [WorklogAdminTab,]

class SiteAdmin(admin.ModelAdmin):
    inlines = [WorklogAdminTab,]

class DisciplineAdmin(admin.ModelAdmin):
    inlines = [PositionAdminTab, ]

class DisputeAdmin(admin.ModelAdmin):
    inlines = [ManHoursChargeAdminTab, EquipmentChargeAdminTab]

admin.site.register(EntryDate)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Region)
admin.site.register(Site, SiteAdmin)
admin.site.register(Rate)
admin.site.register(DayRate)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(EquipmentCharge)
admin.site.register(ManHoursCharge)
admin.site.register(RateSheet)
admin.site.register(Worklog, WorklogAdmin)
admin.site.register(Dispute, DisputeAdmin)