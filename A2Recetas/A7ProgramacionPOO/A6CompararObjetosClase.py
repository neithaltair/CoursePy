# A7-6: Comparar objetos

# SE REALIZA SOBRE ESCRITURA DE LOS METODOS PARA REALIZAR MODIFICACIONES
# EN LAS COMPARACIONES DE LOS OBJETOS (NUMEROS COMPLEJOS)
class NumeroComplejo:
    def __init__(self, real, imaginaria):
        self.real = real
        self.imaginaria = imaginaria

    def __lt__(self, other):
        if self.real < other.real and self.imaginaria < other.imaginaria:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.real > other.real and self.imaginaria > other.imaginaria:
            return True
        else:
            return False

    def __eq__(self, other):
        return self.real == other.real and self.imaginaria == other.imaginaria

num1 = NumeroComplejo(3,5)
num2 = NumeroComplejo(2,1)
num3 = NumeroComplejo(3,5)

print(num1>num2)
print(num1==num3)