#COMPROBAR SI DOS ELEMENTOS SON IGUALES ELEMENTO A ELEMENTO BAJO UN GRADO DE TOLERANCIA
import numpy as np

#allclose() permite hacer la coprobacion

comp = np.allclose([1e10, 1e-7], [1.0001e10, 1e-8])
print("Realiza la comprobacion",comp)