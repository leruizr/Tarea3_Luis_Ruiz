# Solicitar el ingreso del afiliado
ingreso = float(input("Ingrese el ingreso mensual del afiliado en salarios mínimos: "))

# Determinar la cuota moderadora según el rango de ingresos
if ingreso < 2:
    cuota = 4000
else:
    if ingreso <= 5:
        cuota = 15000
    else:
        cuota = 40000

# Mostrar el valor de la cuota moderadora
print(f"El valor de la cuota moderadora es: ${cuota}")