from django.test import TestCase
from .models import Annuity

# Create your tests here.
class AnnuityTestCase(TestCase):
    def setUp(self):
        #standard annuity case
        Annuity.objects.create(amount=1000, duration=240)
        Annuity.objects.create(amount=500, duration=360)

    def test_annuities_created(self):
        """Annuities are correctly created"""
        first = Annuity.objects.get(amount=1000)
        second = Annuity.objects.get(amount=500)
        self.assertEqual(first.duration, 240)
        self.assertEqual(second.duration, 360)
