from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('temapi.api.urls')),
    path('auth/', include('authapp.urls'))
]
