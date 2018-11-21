#Testes de unidade para este modulo
import unittest
from bezout import bezout
from minimizeCoefficientsBezout import minimizeCoefficientsBezout

class TestBezout(unittest.TestCase):

    def setUp(self):
        pass

    def test_case_10_3(self):
        self.assertEqual(bezout(10,3), {'coeff0': 1, 'coeff1': -3, 'gcd': 1})
    def test_case_3_10(self):
        self.assertEqual(bezout(3,10), {'coeff0': -3, 'coeff1': 1, 'gcd': 1})
    def test_case_92_12(self):
        self.assertEqual(bezout(92,12), {'coeff0': -1, 'coeff1': 8, 'gcd': 4})
    def test_case_326_1256(self):
        self.assertEqual(bezout(326,1256), {'coeff0': 131, 'coeff1': -34, 'gcd': 2})
    def test_case_5_7_3(self):
        self.assertEqual(bezout(5,7), {'coeff0': 3, 'coeff1': -2, 'gcd': 1})

class TestMinimizeCoefficients(unittest.TestCase):

    def setUp(self):
        pass

    def test_case_10_3_2(self):
        self.assertEqual(minimizeCoefficientsBezout(10,3,2), {'coeff0': -1, 'coeff1': 4})
    def test_case_3_10_2(self):
        self.assertEqual(minimizeCoefficientsBezout(3,10,2), {'coeff0': 4, 'coeff1': -1})
    def test_case_326_1256(self):
        self.assertEqual(minimizeCoefficientsBezout(326,1256,1), False)
    def test_case_5_7_3(self):
        self.assertEqual(minimizeCoefficientsBezout(5,7,3), {'coeff0': 2, 'coeff1': -1})
    def test_case_7_5_3(self):
        self.assertEqual(minimizeCoefficientsBezout(7,5,3), {'coeff0': -1, 'coeff1': 2})
    def test_case_7_5_9(self):
        self.assertEqual(minimizeCoefficientsBezout(7,5,9), False)
    def test_case_negative_7_5_3(self):
        self.assertEqual(minimizeCoefficientsBezout(-7,5,3), False)
    def test_case_7_negative_5_3(self):
        self.assertEqual(minimizeCoefficientsBezout(7,-5,3), False)
    def test_case_7_5_negative_3(self):
        self.assertEqual(minimizeCoefficientsBezout(7,5,-3), False)


if __name__ == "__main__":
    unittest.main()
