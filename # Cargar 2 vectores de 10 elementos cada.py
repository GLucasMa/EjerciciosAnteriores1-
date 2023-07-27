## Cargar 2 vectores de 10 elementos cada uno de numeros aleatorios (1 al 20) y generar un 3 vector de 10 elementos que contenga la suma de ambos
#en las posiciones pares y la multiplicacion en las posiciones impares.
import random

vec1 = []
vec2 = []
vec3 = []
num = 0
msj = ""
for i in range(0, 10): # lo hacemos con for por que no tenemos ninguna condicion, ya tenemos los 10 numeros definidos.
    num = random.randint(1, 20)
    vec1.append(num) 
    num = random.randint(1, 20)
    vec2.append(num)
for i in range(0, 10):
    if(i % 2 == 0):
        vec3.append(vec1[i] + vec2[i])
    else:
        vec3.append(vec1[i] * vec2[i])

for i in range(0, 10):
    if(i % 2 == 0):
        msj = str(vec1[i]) + "+" + str(vec2[i]) + "=" + str(vec3[i])
    else:
        msj = str(vec1[i]) + "*" + str(vec2[i]) + "=" + str(vec3[i])
    print(msj)