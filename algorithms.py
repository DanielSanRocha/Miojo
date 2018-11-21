 # Dado dois inteiros (a,b) positivos esta funcao retorna um objeto da forma
 # {'coeff0': x, 'coeff1': y, 'gcd': d} d é o mdc entre a e b # -*- coding: utf-8 -*-
 # x e y é um par de inteiros satisfazendo a*x + b*y = mdc(a,b), |x| < b e |y| < a.

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


#Testes de unidade para esse modulo
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

if __name__ == "__main__":
    unittest.main()
