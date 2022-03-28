from django.contrib import admin
from django.urls import path, include
from find_route.views import about

from routes.views import home, find_routes, add_route, save_route

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('cities/', include(('cities.urls', 'cities'))),
    path('trains/', include(('trains.urls', 'trains'))),

    path('', home, name='home'),
    path('find_routes/', find_routes, name='find_routes'),
    path('add_route/', add_route, name='add_route'),
    path('save_route/', save_route, name='save_route'),
]
