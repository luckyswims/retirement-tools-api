from django.test import TestCase
from .models import Annuity
from .pv import pv, pvSingleRate, pvPPARates

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

class PVFunctionsTestCase(TestCase):
    def test_pv_single_rate(self):
        """Base PV function works correctly"""
        first = pvSingleRate(100, 5, 0.05)
        second = pvSingleRate(200, 10, 0.1)
        self.assertAlmostEqual(first, 454.5951, places=4)
        self.assertAlmostEqual(second, 1351.8048, places=4)

    def test_pv_ppa_rates(self):
        """Three Segment Rate PV function works correctly"""
        #Longer than 20 years
        first = pvPPARates(100, 360, [0.01, 0.025, 0.05])
        #Less than 20 years, more than 5
        second = pvPPARates(100, 180, [0.01, 0.025, 0.05])
        #Less than 5 years
        third = pvPPARates(100, 48, [0.01, 0.025, 0.05])
        self.assertAlmostEqual(first, 26433.9046, places=4)
        self.assertAlmostEqual(second, 15983.1710, places=4)
        self.assertAlmostEqual(third, 4707.6829, places=4)

class PVTestCase(TestCase):
    def test_pv_single_annuity(self):
        singleAnnuity = {
            "annuities": [{
                "amount": 100,
                "duration": 5,
                "rates": 0.05
            }]
        }
        singlePPAAnnuity = {
            "annuities": [{
                "amount": 100,
                "duration": 360,
                "rates": [0.01, 0.025, 0.05]
            }]
        }
        single = pv(singleAnnuity)
        singlePPA = pv(singlePPAAnnuity)
        self.assertEqual(single, 454.60)
        self.assertEqual(singlePPA, 26433.9)
    
    def test_pv_multiple_annuities(self):
        multipleAnnuity = {
            "annuities": [{
                "amount": 100,
                "duration": 5,
                "rates": 0.05
            },
            {
                "amount": 200,
                "duration": 10,
                "rates": 0.1
            }]
        }
        multiplePPAAnnuity = {
            "annuities": [{
                "amount": 100,
                "duration": 360,
                "rates": [0.01, 0.025, 0.05]
            },
            {
                "amount": 100,
                "duration": 180,
                "rates": [0.01, 0.025, 0.05]
            },
            {
                "amount": 100,
                "duration": 48,
                "rates": [0.01, 0.025, 0.05]
            }]
        }
        
        multiple = pv(multipleAnnuity)
        multiplePPA = pv(multiplePPAAnnuity)
        self.assertEqual(multiple, 1806.4)
        self.assertEqual(multiplePPA, 47124.75)
        
