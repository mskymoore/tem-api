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
    path('worklog/<client>/<date>', WorklogViewSet.as_view({"get": "list"})),
    path('worklog/<client>/<start_date>/<end_data>',
         WorklogViewSet.as_view({"get": "list"})),
    path('worklog/<client>/<site>', WorklogViewSet.as_view({"get": "list"})),
    path('worklog/<site>', WorklogViewSet.as_view({"get": "list"})),
    path('worklog/<site>/<client>', WorklogViewSet.as_view({"get": "list"})),
    path('worklog/<site>/<date>', WorklogViewSet.as_view({"get": "list"})),
    path('worklog/<site>/<start_date>/<end_date>',
         WorklogViewSet.as_view({"get": "list"})),
    path('dispute/<worklog>', DisputeViewSet.as_view({"get": "list"})),
    path('dispute/<client>', DisputeViewSet.as_view({"get": "list"})),
    path('dispute/<client>/<is_resolved>',
         DisputeViewSet.as_view({"get": "list"})),
    path('ratesheet/<client>', RateSheetViewSet.as_view({"get": "list"})),
    path('ratesheet/<client>/<region>',
         RateSheetViewSet.as_view({"get": "list"})),
    path('ratesheet/<name>', RateSheetViewSet.as_view({"get": "list"})),
    path('equipcharge/<created_by>',
         EquipmentChargeViewSet.as_view({"get": "list"})),
    path('equipcharge/<created_by>/<date>',
         EquipmentChargeViewSet.as_view({"get": "list"})),
    path('equipcharge/<equipment>',
         EquipmentChargeViewSet.as_view({"get": "list"})),
    path('equipcharge/<equipment>/<date>',
         EquipmentChargeViewSet.as_view({"get": "list"})),
    path('equipcharge/<client>',
         EquipmentChargeViewSet.as_view({"get": "list"})),
    path('equipcharge/<client>/<region>',
         EquipmentChargeViewSet.as_view({"get": "list"})),
    path('equipcharge/<client>/<date>',
         EquipmentChargeViewSet.as_view({"get": "list"})),
    path('manhrscharge/<created_by>',
         ManHoursChargeViewSet.as_view({"get": "list"})),
    path('manhrscharge/<created_by>/<date>',
         ManHoursChargeViewSet.as_view({"get": "list"})),
    path('manhrscharge/<employee>',
         ManHoursChargeViewSet.as_view({"get": "list"})),
    path('manhrscharge/<employee>/<date>',
         ManHoursChargeViewSet.as_view({"get": "list"})),
    path('manhrscharge/<client>',
         ManHoursChargeViewSet.as_view({"get": "list"})),
    path('manhrscharge/<client>/<date>',
         ManHoursChargeViewSet.as_view({"get": "list"}))


]
