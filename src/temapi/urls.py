from django.urls import path, include

from temapi.views import DisciplineViewSet, PositionViewSet, reset_user_password
from temapi.views import EmployeeViewSet, ClientViewSet, RegionViewSet
from temapi.views import SiteViewSet, RateViewSet, EquipmentViewSet
from temapi.views import DayRateViewSet, RateSheetViewSet, WorklogViewSet
from temapi.views import DisputeViewSet, EquipmentChargeViewSet, ManHoursChargeViewSet
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


router = NestedDefaultRouter()
router.register(r'discipline', DisciplineViewSet, basename='discipline')
router.register(r'position', PositionViewSet, basename='position')

employee = router.register(r'employee', EmployeeViewSet)
employee.register(
    r'position',
    PositionViewSet,
    basename='employee-position',
    parents_query_lookups=['employee'],
)

employee.register(
    r'worklog',
    WorklogViewSet,
    basename='employee-worklog',
    parents_query_lookups=['employee']
)

client = router.register(r'client', ClientViewSet)
client.register(
    r'worklog',
    WorklogViewSet,
    basename='client-worklog',
    parents_query_lookups=['client']
)
client.register(
    r'ratesheet',
    RateSheetViewSet,
    basename='client-ratesheet',
    parents_query_lookups=['client']
)


router.register(r'region', RegionViewSet, basename='region')
router.register(r'site', SiteViewSet, basename='site')
router.register(r'rate', RateViewSet, basename='rate')
router.register(r'equipment', EquipmentViewSet, basename='equipment')
router.register(r'dayrate', DayRateViewSet, basename='dayrate')
router.register(r'ratesheet', RateSheetViewSet, basename='ratesheet')
router.register(r'worklog', WorklogViewSet, basename='worklog')
router.register(r'dispute', DisputeViewSet, basename='dispute')
router.register(r'equipcharge', EquipmentChargeViewSet)
router.register(r'manhrscharge', ManHoursChargeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reset_password/<uid>/<token>',
         reset_user_password, name='reset-pasword'),
]
