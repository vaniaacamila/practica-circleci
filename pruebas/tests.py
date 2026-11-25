
from django.test import TestCase

class PruebasIniciales(TestCase):

    def test_suma_correcta(self):
        resultado = 2 + 2
        self.assertEqual(resultado, 4)

    def test_multiplicacion_correcta(self):
        resultado = 3 * 3
        self.assertEqual(resultado, 9)
        
        
    def test_suma_incorrecta(self):
        resultado = 2 + 2
        self.assertEqual(resultado, 5)