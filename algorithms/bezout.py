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
