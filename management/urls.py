from django.contrib import admin
from django.urls import path, include

from apps.user import urls
from apps.user.views import first_page

urlpatterns = [
    path('', first_page, name='first_page'),
    path('admin/', admin.site.urls),
    path('main/', include(urls), name='main_page')
]
