from bezout import bezout

# Dado tres inteiros (a,b,c) positivos com c < a e c < b, esta funcao retorna
#um objeto da forma
# {'coeff0': x, 'coeff1': y} com x,y inteiros saisfazendo:
# a*x + b*y = c e tal que max{|a*x|,|b*y|} e o menor possivel, se possivel.
# Caso nao seja possivel expressar c desta forma ou
# a input nao satisfaca a condicao requerida esta funcao retorna False.
def minimizeCoefficientsBezout(a, b, c):

   if (a <= 0 or b <= 0 or c<= 0 or c >= a or c>= b):
       return False

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
