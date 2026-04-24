alfabeto = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
clave = "URJC"
textoCifrado = "udXPalb"
textoCifrar = "Amongus"

def cifrar():
    i=0
    for letra in textoCifrar:
        cif = alfabeto.index(letra)
        cla = alfabeto.index(clave[i])
        newPos = (cif + cla) % len(alfabeto)
        i = (i + 1) % len(clave)
        print(alfabeto[newPos], end="")
    print()

def descifrar():
    i=0
    for letra in textoCifrado:
        cif = alfabeto.index(letra)
        cla = alfabeto.index(clave[i])
        oldPos = (cif - cla) % len(alfabeto)
        i = (i + 1) % len(clave)
        print(alfabeto[oldPos],end="")
    print()

cifrar()      
descifrar()


