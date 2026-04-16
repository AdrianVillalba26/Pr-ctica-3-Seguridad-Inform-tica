listaAlf = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
codigo = input("Inserte codigo: ")

i = 1

for _ in range(1,26):
    for letra in codigo:
        if letra in listaAlf:
            indice = listaAlf.index(letra)
            nueva_letra = listaAlf[(indice + i) % 26]
            print(nueva_letra,end="")
        else:
            print(letra,end="")
    print("")
    i += 1