from django.urls import path, include

from temapi.views import DisciplineViewSet, PositionViewSet, reset_user_password
from temapi.views import EmployeeViewSet, ClientViewSet, RegionViewSet
from temapi.views import SiteViewSet, RateViewSet, EquipmentViewSet
from temapi.views import DayRateViewSet, RateSheetViewSet, WorklogViewSet
from temapi.views import DisputeViewSet, EquipmentChargeViewSet, ManHoursChargeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'discipline', DisciplineViewSet)
router.register(r'position', PositionViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'client', ClientViewSet)
router.register(r'region', RegionViewSet)
router.register(r'site', SiteViewSet)
router.register(r'rate', RateViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'dayrate', DayRateViewSet)
router.register(r'ratesheet', RateSheetViewSet, basename='ratesheet')
router.register(r'worklog', WorklogViewSet, basename='worklog')
router.register(r'dispute', DisputeViewSet)
router.register(r'equipcharge', EquipmentChargeViewSet)
router.register(r'manhrscharge', ManHoursChargeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reset_password/<uid>/<token>',
         reset_user_password, name='reset-pasword'),
]
