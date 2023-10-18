
from django.contrib import admin
from django.urls import path, include

from apps.user import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include(urls))
]