class Persona ():

    def __init__(self, nombre, edad, residencia):
    
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print("Nombre = ", self.nombre, "\nEdad = ",self.edad, "\nResidencia = ",self.residencia)


#Establecemos que el empleado herede de la clase persona
class Empleado (Persona):
    
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()

        print("Salario = ", self.salario, "\nAntiguedad = ", self.antiguedad)

    
Antonio = Empleado(1000, 20, "Antonio", 55, "Colombia")

Antonio.descripcion()

#USO DEL IS INSTANCE
print(isinstance(Antonio, Empleado))