from django.contrib import admin
from django.urls import path, include

app_name = 'GILTI'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('GILTI/', include('GILTI.urls')),
]
