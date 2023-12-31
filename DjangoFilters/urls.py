from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from api import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("api.urls"), name="api"),
]
