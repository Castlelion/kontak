from django.contrib import admin
from .models import Sekolah     

# Register your models here.
class namaSekolah(admin.ModelAdmin):
    list_display = ['Nama','Email','Web','Hp','Alamat','Jenis_Sekolah']

admin.site.register(Sekolah,namaSekolah)