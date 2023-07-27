def obtenerColor(cod):
    color=""
    if(cod==0):
        color="VERDE"
    if (cod==1 or cod==3 or cod==5):
        color="ROJO"
    if (cod==2 or cod==4 or cod==6):
        color="NEGRO"
    if (cod==7 or cod==9 or cod== 12 or cod==14):
        color="ROJO"
    if (cod==8 or cod==18 or cod==19 or cod ==21):
        color="ROJO"
        
    return color