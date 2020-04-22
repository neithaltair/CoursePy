import unittest

def multiplicar(num1, num2):
    return num1*num2

resultado = multiplicar(2,8)
print(resultado)



class pruebas(unittest.TestCase):

    def test(self):
        self.assertEqual(multiplicar(2,5),10)


if __name__ == '__main__':
    unittest.main()