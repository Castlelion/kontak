from django.test import TestCase
from siswa.models import Siswa

# Create your tests here.
class TestModels(TestCase):

    def setUp(self):
        self.nama1 = Siswa.objects.create(
            Nama="Aldi",
            Email="aldi@gmail.com"
        )

    # def test_project_is_assigned_slug_on_creation(self):
    #     self.assertEqual(self.nama1.slug, 'aldi-1')
        