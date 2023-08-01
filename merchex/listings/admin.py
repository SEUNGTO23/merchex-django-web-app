from django.contrib import admin

# Register your models here.
from listings.models import Band
from listings.models import Liste

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre', 'active')
admin.site.register(Band, BandAdmin)

class ListeAdmin(admin.ModelAdmin):
    list_display = ('titre', 'sold', 'type', 'band')
admin.site.register( Liste, ListeAdmin)