
from django.contrib import admin
from django.urls import path, include

from django.contrib import admin


admin.site.site_header = 'Safe-Zone'
admin.site.site_title = 'Safe-Zone admin'
admin.site.index_title = 'Safe-Zone administration'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
