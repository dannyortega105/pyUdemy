import unittest
import cambiar_texto

class Prueba (unittest.TestCase):

    def test_mayusculas(self):
        palabra = "Buen dia"
        resultado = cambiar_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "BUEN DIA")

if __name__ == '__main__':
    unittest.main()