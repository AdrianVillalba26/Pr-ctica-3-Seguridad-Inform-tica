textoCifrado="({!+8b*+"
textoParaCifrar = "seguridad"
clave="XOR"

def descifrar():
    i = 0
    for letra in textoCifrado:
        decod= ord(letra) ^ ord(clave[i])
        i = (i + 1) % len(clave)
        print(chr(decod), end="")
    print()

def cifrar():
    i = 0
    for letra in textoParaCifrar:
        decod= ord(clave[i]) ^ ord(letra)
        i = (i + 1) % len(clave)
        print(chr(decod), end="")

descifrar()
cifrar()