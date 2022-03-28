from django.contrib import admin
from django.urls import path, include
from find_route.views import about

from routes.views import home, find_routes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('cities/', include(('cities.urls', 'cities'))),
    path('trains/', include(('trains.urls', 'trains'))),

    path('', home, name='home'),
    path('find_routes/', find_routes, name='find_routes'),
]
