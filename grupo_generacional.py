# Solicitar la edad de la persona
edad = int(input("Ingrese su edad: "))

# Determinar el grupo generacional según la edad
if edad <= 12:
    grupo = "Niño"
elif 13 <= edad <= 17:
    grupo = "Adolescente"
elif 18 <= edad <= 34:
    grupo = "Joven"
elif 35 <= edad <= 63:
    grupo = "Adulto"
else:
    grupo = "Adulto mayor"

# Mostrar el grupo generacional
print(f"Perteneces al grupo generacional: {grupo}")