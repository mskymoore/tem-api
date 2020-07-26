from django.urls import path, include

from temapi.views import DisciplineViewSet, PositionViewSet, reset_user_password
from temapi.views import EmployeeViewSet, ClientViewSet, RegionViewSet
from temapi.views import SiteViewSet, RateViewSet, EquipmentViewSet
from temapi.views import DayRateViewSet, RateSheetViewSet, WorklogViewSet
from temapi.views import DisputeViewSet, EquipmentChargeViewSet, ManHoursChargeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'dis', DisciplineViewSet)
router.register(r'pos', PositionViewSet)
router.register(r'emp', EmployeeViewSet)
router.register(r'cli', ClientViewSet)
router.register(r'reg', RegionViewSet)
router.register(r'sit', SiteViewSet)
router.register(r'rat', RateViewSet)
router.register(r'eqp', EquipmentViewSet)
router.register(r'drt', DayRateViewSet)
router.register(r'rsh', RateSheetViewSet)
router.register(r'wrk', WorklogViewSet)
router.register(r'disp', DisputeViewSet)
router.register(r'eqpchrg', EquipmentChargeViewSet)
router.register(r'mnhrschrg', ManHoursChargeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reset_password/<uid>/<token>',
         reset_user_password, name='reset-pasword'),
]
