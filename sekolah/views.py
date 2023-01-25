from django.shortcuts import render
from .models import Sekolah
# Create your views here.
def Sekolah(request):
    return render(request, 'pkl/test.html')