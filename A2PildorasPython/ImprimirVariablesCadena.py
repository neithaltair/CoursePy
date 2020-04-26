nombre = 'Antonio'
print("Buenos dias "+nombre)

# Format
edad = 18
print("Buenos dias {}, feliz {} cumpleaños".format(nombre,edad))

# Format con variable
resultado = 10/3 
print(resultado)

# Imprimir cantidad especifica de decimales
print("El resultado es {r:1.3f}".format(r=resultado))

# Format corto 
print(f'Buenos dias {nombre}, feliz {edad}')
print(f'El resultado es: {resultado:1.5f}')
