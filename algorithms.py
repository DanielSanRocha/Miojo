 # Dado dois inteiros (a,b) positivos esta funcao retorna um objeto da forma
 # {'coeff0': x, 'coeff1': y, 'gcd': d} d é o mdc entre a e b # -*- coding: utf-8 -*-
 # x e y é um par de inteiros satisfazendo a*x + b*y = mdc(a,b)

def bezout(a, b):

    # O loop principal do algoritmo de euclides (https://en.wikipedia.org/wiki/Euclidean_algorithm)
    if a > b:
        d = [a,b]
        swap = False
    else:
        d = [b,a]
        swap = True

    # Coeficientes tais que d[0] = s[0] * d[0] + s[1] * d[1], d[1] = t[0] * d[0] + t[1] * d[1]
    s = [1,0]
    t = [0,1]

    while (d[1] != 0):
        q = d[0] // d[1]
        temp = d[1]
        d[1] = d[0] - q * d[1]
        d[0] = temp

        # Salvando os novos coeficientes
        temp = [t[0],t[1]]
        t[0] = s[0] - q * t[0]
        t[1] = s[1] - q * t[1]
        s = temp

    return {'coeff0': s[1], 'coeff1': s[0], 'gcd': d[0]} if swap else {'coeff0': s[0], 'coeff1': s[1], 'gcd': d[0]}


# Dado três inteiros (a,b,c) positivos com c < a e c < b, esta funcao retorna
#um objeto da forma
# {'coeff0': x, 'coeff1': y} com x,y inteiros saisfazendo:
# a*x + b*y = c e tal que max{|a*x|,|b*y|} e o menor possivel, se possivel.
# Caso não seja possivel expressar c desta forma esta funcao retorna False.
def minimizeCoefficientsBezout(a, b, c):

    bezoutResult = bezout(a,b)
    gcd = bezoutResult['gcd']

    if (c % gcd != 0):
        return False

    coeff0 = bezoutResult['coeff0'] * (c // gcd)
    coeff1 = bezoutResult['coeff1'] * (c // gcd)

    q = coeff0 // b if coeff0 > 0 else coeff0 // b + 1

    # A possible solution
    coeff0 = coeff0 - q * b
    coeff1 = coeff1 + q * a

    if (coeff0 > 0):
        _coeff0 = coeff0 - b
        _coeff1 = coeff1 + a
    else:
        _coeff0 = coeff0 + b
        _coeff1 = coeff1 - a

    maxAbs = max(abs(coeff0),abs(coeff1))
    _maxAbs = max(abs(_coeff0),abs(_coeff1))

    return {'coeff0': _coeff0, 'coeff1': _coeff1} if maxAbs > _maxAbs else {'coeff0': coeff0, 'coeff1': coeff1}

#Testes de unidade para este modulo
import unittest

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


if __name__ == "__main__":
    unittest.main()
