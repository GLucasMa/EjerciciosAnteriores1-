import os
import random
import funcionesRuleta
saldo=10000
msj=""
jugar=True
opcion=0
apuesta=0
bolilla= 0
color=""
colorBolilla=""




while (jugar==True):
    os.system("cls")
    msj="Su saldo es de " + str(saldo)
    print(msj)
    msj="1->Jugar, 2->Salir"
    print(msj)
    opcion=int(input(""))
    if (opcion==2):
        jugar=False
    if (opcion==1):
        msj="Ingresar valor a apostar: "
        print(msj)
        apuesta=int(input(""))
        if (apuesta <= saldo):
            msj="Elegir color: 1-> verde, 2->Rojo, 3->Negro"
            print(msj)
            opcion=int(input(""))
        bolilla= random.randint(0,6)
        if (opcion ==1):
            color="VERDE"
        if (opcion==2):
            color="ROJO"
        if (opcion==3):
            color="NEGRO"
        colorBolilla=funcionesRuleta.obtenerColor(bolilla)
        if(color==colorBolilla):
            saldo=(saldo+apuesta)
        else:
            saldo=(saldo-apuesta)
            print("Perdió")
        msj="El número es " + str(bolilla)+" el color es: "+ colorBolilla 
        print(msj)
        car=input("Presiones una tecla para continuar")


