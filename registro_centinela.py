# Caso 1 Registro Centinela

# input

codigo = int(input("Digite el código del estudiante: "))
nota_parcial1 = float(input("Digite la nota del parcial 1: "))
nota_parcial2 = float(input("Digite la nota del parcial 2: "))
nota_parcial3 = float(input("Digite la nota del parcial 3: "))

# processing
cant_reprobados = 0

while (codigo != 0):
    nota_final = (nota_parcial1 + nota_parcial2 + nota_parcial3) / 3
    print("El estudiante de código " + str(codigo) + " obtuvo una nota final de " + str(nota_final))

    if (nota_final < 3.0):
        cant_reprobados = cant_reprobados + 1

    codigo = int(input("Digite el código del estudiante: "))
    nota_parcial1 = float(input("Digite la nota del parcial 1:"))
    nota_parcial2 = float(input("Digite la nota del parcial 2:"))
    nota_parcial3 = float(input("Digite la nota del parcial 3:"))

print("Cantidad estudiantes reprobados: " + str(cant_reprobados))