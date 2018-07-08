from django.test import TestCase
from .models import *

class CalculationTest(TestCase):
    def test_calculations_correct(self):

        c = Client(name='client', exp_alloc=25, US_Rate=73, tax_inc=550, id=1)
        c.save()
        sub1 = Subsidiary(client=c, name='sub1', country='', ownership=55, ref='', gross_income=950, eci=-5, sub_f=-15, rp_div=-20, for_tax=132, qbai=44, int_exp=74)
        sub2 = Subsidiary(client=c, name='sub2', country='', ownership=35, ref='', gross_income=-30, eci=0, sub_f=-17, rp_div=-38, for_tax=45, qbai=23, int_exp=104)

        sub2.save()
        sub1.save()

        

        url = reverse('GILTI:subdetail', kwargs={'pk':c.id})
        response = self.client.get(url)
        sub_data = response.context['sub_data']

        print(sub_data[2])
        
        
        accurate_data=[
                [0, 0, 0, 0, 0, -30, -30, 45, 23, '', 104, 0, 0, 0, 0, 0, -11, -11, 16, 8, '', 36],
                [950, -5, -15, -20, 910, 0, 910, 132, 44, '', 74, 523, -3, -8, -11, 501, 0, 501,  73, 24, '', 41],
                [950, -5, -15, -20, 910, -30, 880, 0, 67, 7, 178, 523, -3, -8, -11, 501, -11, 490, 0, 32, 3, 77, 0, 490, 97.90, 0, 0, 550, 490, 0, 1040, 0, 1040, 25, 1065, 224, 385, 0, 385, 0, 73, 550, 0, 0, 0]
            ]

        print(accurate_data[2])

        self.assertEqual(sub_data, accurate_data)
        