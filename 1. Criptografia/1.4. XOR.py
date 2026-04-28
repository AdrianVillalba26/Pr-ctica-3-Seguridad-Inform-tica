textoCifrado="({!+8b*+"
clave="XOR"
i = 0
for letra in textoCifrado:
    decod= ord(letra) ^ ord(clave[i])
    i = (i + 1) % len(clave)
    print(chr(decod), end="")