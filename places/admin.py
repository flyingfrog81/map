from django.contrib import admin
from places.models import Place

class PlaceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date', 'lat', 'lon', 'description'], 'classes': ['collapse']}),    
    ]
    list_display = ('name', 'lat', 'lon', 'description', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    search_fields = ['name']

admin.site.register(Place, PlaceAdmin)
