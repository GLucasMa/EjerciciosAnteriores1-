#Impirmir el mayor es 8 y se repite dos veces
vec = [4,5,7,7,7,8,8,4,5]
mayor = 0
repite = 0
msj = ""
for i in range(0, len(vec)): 
    if(i == 0):
        mayor = vec[i]
for i in range(0, len(vec)):
    if(vec[i] > mayor):
        mayor = vec[i] #el mayor
for i in range(0, len(vec)):
    if(mayor == vec[i]):
        repite = repite + 1 #contador para saber cuantas veces
print(vec)
msj = "El mayor es " + str(mayor) + " y se repite " + str(repite) + " veces"
print(msj)