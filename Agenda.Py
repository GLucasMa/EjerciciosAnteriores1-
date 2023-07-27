import os
import funciones
Msj=""
Dni=""
Nombre=""
Telefono=""
VecDni=[]
VecNom=[]
VecTelefono=[]
opcion= 0
fin = False

while(fin==False):
    msj= "1->Agregar, 2->Modificar, 3->Eliminar, 4->Imprimir, 5->Salir "
    print (msj)
    opcion= int(input(""))
    if (opcion==5):
        fin= True

    if(opcion==1):
        msj= "Ingresar nombre"
        print (msj)
        Nombre= input("")
        msj= "Ingresar Dni"
        print (msj)
        Dni= input("")
        msj= "Ingresar telefono"
        print(msj)
        Telefono= input("")
        VecDni.append(Dni)
        VecNom.append(Nombre)
        VecTelefono.append(Telefono)
        
        
    if(opcion==4):
        funciones.imprimir(VecDni, VecNom, VecTelefono)
        car=input("presionar enter")


    car= ""
    if (opcion==2):
            print ("Ingresar dni del cliente a modificar")
            Dni= input("")
            print ("Ingresar nombre")
            Nombre= input("")
            print ("Ingresar telefono")
            Telefono= input("")
            funciones.modificar(Dni, Nombre, Telefono, VecDni, VecNom, VecTelefono)
            car= input("Presione enter para continuar")
    

    if(opcion==3):
        msj="Ingresar Dni a borrar"
        print (msj)
        Dni= input ("")
        funciones.eliminar(Dni, VecDni, VecNom, VecTelefono)
        car= input("presionar enter")


