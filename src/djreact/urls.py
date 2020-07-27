from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from djreact.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('temapi.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('schema/', get_schema_view(
        title="TEM API",
        description="API for Time and Equipment Tracking",
        version="0.0.1"
    ), name='openapi-schema')
]

if DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
