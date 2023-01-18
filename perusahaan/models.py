from django.db import models
from django.utils.translation import gettext_lazy as _

class JenisPerusahaan(models.TextChoices):
    PT ='PT', _('PT')
    CV ='CV', _('CV')
    Firma ='F', _('Firma')
    KOPERASI ='K', _('Koperasi')
    Persero ='PR', _('Persero')
    PERSEORANGAN ='PG', _('Perseorangan')

class Perusahaan(models.Model):
    Nama = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Web = models.CharField(max_length=100, blank=True, null=True)
    Hp = models.CharField(max_length=20)
    Alamat = models.TextField(max_length=100)
    Jenis_Perusahaan = models.CharField(
        max_length=2,
        choices=JenisPerusahaan.choices,
    )
    # sekolah

    # default
    # create_by =
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Nama

    class Meta:
        ordering = ['-id']
        


# Create your models here.
