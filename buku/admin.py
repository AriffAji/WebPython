from django.contrib import admin
from .models import *
# Register your models here.

class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul', 'penulis','penerbit', 'Published']
    search_fields = ['judul', 'penulis','penerbit','jumlah ']
    list_filter = ('kelompok_id',)
    list_per_page = 5
admin.site.register(Buku, BukuAdmin)
admin.site.register(Kelompok)