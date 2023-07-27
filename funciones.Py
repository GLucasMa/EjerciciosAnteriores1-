
from re import I

def imprimir(vec1, vec2, vec3):
    msj= ""
    for i in range(0, len(vec1)):
        print ("--------------------------")
        msj= "Dni " + vec1[i]
        print (msj)
        msj= "Nombre " + vec2[i]
        print (msj)
        msj= "Telefono " + vec3[i]
        print (msj)

def eliminar(Dni, vec1, vec2, vec3):
    msj= ""
    b=0
    indice= 0
    for i in range(0, len(vec1)):
        if (Dni==vec1[i]):
            indice= i
            b=1
    if(b==1):
        vec1.pop(indice)
        vec2.pop(indice)
        vec3.pop(indice)
        MSJ= "Contacto Borrado"
    else:
        msj= "No existe DNI"
        print (msj)
    
def modificar (Dni, Nombre, Telefono, vec1, vec2, vec3):
    b=0
    for i in range(0, len(vec1)):
        if(Dni == vec1[i]):
            vec2[i] = Nombre
            vec3[i]= Telefono
            b=1
        if(b==1):
            print ("cliente actualizado")
        else:
            print ("cliente inexistente")
