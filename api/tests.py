from django.test import TestCase
from .models import Annuity
from .pv import pv, pvSingleRate, pvPPARates, deferralSingleRate, deferralPPA, pvPPADeferred

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
        self.assertAlmostEqual(first, 495.9588, places=4)
        self.assertAlmostEqual(second, 1930.2819, places=4)

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
        
    def test_deferral_single_rate(self):
        """Base deferral works correctly"""
        first = deferralSingleRate(495.96, 0.05, 5)
        second = deferralSingleRate(1930.28, 0.1, 5)
        self.assertAlmostEqual(first, 485.9793, places=4)
        self.assertAlmostEqual(second, 1855.1258, places=4)

    def test_deferral_ppa(self):
        """Three Segment Rate deferral works correctly""" 
        first = deferralPPA(2377.26, [0.01, 0.025, 0.05], 24)
        second = deferralPPA(18644.88, [0.01, 0.025, 0.05], 72)
        third = deferralPPA(15356.66, [0.01, 0.025, 0.05], 252)
        self.assertAlmostEqual(first, 2330.4186, places=4)
        self.assertAlmostEqual(second, 17307.2815, places=4)
        self.assertAlmostEqual(third, 9608.2130, places=4)
    
    def test_pv_ppa_deferred(self):
        """Three Segment Rate PV with deferral works correctly"""
        first = pvPPADeferred(100, 24, [0.01, 0.025, 0.05], 24)
        second = pvPPADeferred(100, 180, [0.01, 0.025, 0.05], 24)
        third = pvPPADeferred(100, 240, [0.01, 0.025, 0.05], 24)
        fourth = pvPPADeferred(100, 240, [0.01, 0.025, 0.05], 72)
        fifth = pvPPADeferred(100, 240, [0.01, 0.025, 0.05], 252)
        self.assertAlmostEqual(first, 2330.4207, places=4)
        self.assertAlmostEqual(second, 15348.2482, places=4)
        self.assertAlmostEqual(third, 19310.8738, places=4)
        self.assertAlmostEqual(fourth, 17307.2798, places=4)
        self.assertAlmostEqual(fifth, 9608.2100, places=4)
        
class PVTestCase(TestCase):
    def test_pv_single_annuity(self):
        """PV function works for single annuity single rate"""
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
        self.assertEqual(single, [495.96])
        self.assertEqual(singlePPA, [26433.9])
    
    def test_pv_multiple_annuities(self):
        """PV function works for multiple annuities"""
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
        self.assertEqual(multiple, [495.96, 1930.28])
        self.assertEqual(multiplePPA, [26433.9, 15983.17, 4707.68])
        
    def test_pv_single_deferred(self):
        """PV function works with deferral"""
        singleAnnuity = {
            "annuities": [{
                "amount": 100,
                "duration": 5,
                "rates": 0.05,
                "deferral": 5
            }]
        }
        singlePPAAnnuity = {
            "annuities": [{
                "amount": 100,
                "duration": 240,
                "rates": [0.01, 0.025, 0.05],
                "deferral": 24
            }]
        }
        single = pv(singleAnnuity)
        singlePPA = pv(singlePPAAnnuity)
        self.assertEqual(single, [485.98])
        self.assertEqual(singlePPA, [18998.91])
