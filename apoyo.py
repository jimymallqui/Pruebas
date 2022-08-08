nombres=[]
INF111=[]
INF112=[]
finalizar111 = ""
finalizar112 = ""

while finalizar111 == "":
    no1 = input("Ingrese nombre INF – 111:")
    no2 = int(input("Ingrese la primera nota INF – 111:"))
    INF111.append([no1, no2])
    finalizar111 = input("desea continuar:")

while finalizar112 == "":
    no1 = input("Ingrese nombre INF – 112:")
    no2 = int(input("Ingrese la primera nota INF – 112:"))
    INF112.append([no1, no2])
    finalizar112 = input("desea continuar:")



reprobados=[]
for datoss in INF111:
    if datoss[1] < 51:
        reprobados.append([datoss[0], datoss[1], "INF111"])



for datoss in INF112:
    if datoss[1] < 51:
        reprobados.append([datoss[0], datoss[1], "INF112"])

print(reprobados)

print("este es el maximo de la primera materia: ")
idx, max_value= max(INF111, key=lambda item: item[1])
print('Maximum value:', max_value, "At index:", idx)

print("este es el minimo de la primera materia: ")
idx, max_value= min(INF111, key=lambda item: item[1])
print('Minimum value:', max_value, "At index:", idx)


print("este es el maximo de la segunda materia: ")
idx, max_value= max(INF112, key=lambda item: item[1])
print('Maximum value:', max_value, "At index:", idx)

print("este es el minimo de la primera materia: ")
idx, max_value= min(INF112, key=lambda item: item[1])
print('Minimum value:', max_value, "At index:", idx)