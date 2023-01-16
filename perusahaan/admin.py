from django.contrib import admin
from .models import Perusahaan

# Register your models here.
class namaPerusahaan(admin.ModelAdmin):
    list_display = ['Nama','Email','Web','Hp','Alamat','Jenis_Perusahaan']

admin.site.register(Perusahaan,namaPerusahaan)