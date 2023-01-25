from django.contrib import admin
from django.urls import path, include

from kontak import views

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('siswa/', include('siswa.urls')),
    path('test/', include('sekolah.urls'), name='test'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
