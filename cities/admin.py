from django.contrib import admin
from cities.models import City

admin.site.site_title = 'Это тайтл админки'
admin.site.site_header = 'Это хэдер админки'
admin.site.index_title = 'Это индекс тайтл админки'

admin.site.register(City)
