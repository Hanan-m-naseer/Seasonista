from django.contrib import admin
from .models import Season, Destination

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'best_months')
    list_filter = ('season',)
    search_fields = ('name', 'description')
