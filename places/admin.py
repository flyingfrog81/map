from django.contrib import admin
from places.models import Place, Information

class InfoInline(admin.TabularInline):
    model = Information
    extra = 0

class PlaceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date', 'lat', 'lon', 'description'], 'classes': ['collapse']}),    
    ]
    inlines = [InfoInline]
    list_display = ('name', 'lat', 'lon', 'description', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    search_fields = ['name']

admin.site.register(Place, PlaceAdmin)
