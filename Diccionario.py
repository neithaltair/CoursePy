dicColors = {'blue':'azul','red':'rojo','yellow':'amarillo', 'black':'negro'}

print(dicColors)

# Print for the user the "key"
print(dicColors['blue']) 

# Assign the key in a variable
valor = dicColors["red"]

print(valor)

# Add a new key in the dictionary
dicColors["black"] = "negro"

print(dicColors)

# Remove a key
dicColors.pop("yellow")

print(dicColors) 

# Print the keys 
for content in dicColors:
    print(content)

# Print the keys and the values
for key, values in dicColors.items():
    print("The key and the value ",key+" = "+values)






