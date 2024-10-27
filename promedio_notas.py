# Solicitar las 5 notas al usuario
nota1 = float(input("Ingrese la primer nota   "))
nota2 = float(input("Ingrese la segunda nota   "))
nota3 = float(input("Ingrese la tercer nota   "))
nota4 = float(input("Ingrese la cuarta nota   "))
nota5 = float(input("Ingrese la quinta nota   "))

# Calcular el primedio
suma_notas = nota1 + nota2 + nota3 + nota4 + nota5
promedio = suma_notas / 5

# Mostrar el promedio
print(f"El promedio del estudiante es: {promedio}")

# Determinar si el curso esta aprobado o no
if promedio >= 3:
    print("Curso aprobado")
else:
    print("Curso no aprobado")