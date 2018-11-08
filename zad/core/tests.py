from django.test import TestCase
from django.urls import reverse_lazy

from core.utils import convert_number_to_words


class NumberToWordsViewTest(TestCase):
    def test_get(self):
        response = self.client.get(reverse_lazy('number_to_words'))
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.client.post(reverse_lazy('number_to_words'), data={'number': 1234})
        self.assertEqual(response.status_code, 302)


class NumberToWordsFunctionTest(TestCase):
    def test_ones(self):
        self.assertEqual(convert_number_to_words('0'),
                         'zero')
        self.assertEqual(convert_number_to_words('1'),
                         'jeden')
        self.assertEqual(convert_number_to_words('0008'),
                         'osiem')

    def test_tens(self):
        self.assertEqual(convert_number_to_words('10'),
                         'dziesięć')
        self.assertEqual(convert_number_to_words('15'),
                         'piętnaście')

    def test_twenties(self):
        self.assertEqual(convert_number_to_words('22'),
                         'dwadzieścia dwa')
        self.assertEqual(convert_number_to_words('36'),
                         'trzydzieści sześć')

    def test_hundreds(self):
        self.assertEqual(convert_number_to_words('154'),
                         'sto pięćdziesiąt cztery')
        self.assertEqual(convert_number_to_words('189'),
                         'sto osiemdziesiąt dziewięć')

    def test_thousands(self):
        self.assertEqual(convert_number_to_words('1025'),
                         'tysiąc dwadzieścia pięć')
        self.assertEqual(convert_number_to_words('2018'),
                         'dwa tysiące osiemnaście')
        self.assertEqual(convert_number_to_words('3273'),
                         'trzy tysiące dwieście siedemdziesiąt trzy')
        self.assertEqual(convert_number_to_words('7043'),
                         'siedem tysięcy czterdzieści trzy')
        self.assertEqual(convert_number_to_words('12656'),
                         'dwanaście tysięcy sześćset pięćdziesiąt sześć')
        self.assertEqual(convert_number_to_words('145712'),
                         'sto czterdzieści pięć tysięcy siedemset dwanaście')
        self.assertEqual(convert_number_to_words('23424351'),
                         'dwadzieścia trzy miliony czterysta dwadzieścia cztery tysiące trzysta pięćdziesiąt jeden')
        self.assertEqual(convert_number_to_words('867992057303'),
                         'osiemset sześćdziesiąt siedem miliardów dziewięćset dziewięćdziesiąt dwa miliony '
                         'pięćdziesiąt siedem tysięcy trzysta trzy')
