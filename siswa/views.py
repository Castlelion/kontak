from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Siswa

class IndexSiswa(ListView):
    queryset = Siswa.objects.all()
