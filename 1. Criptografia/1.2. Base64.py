import base64
textoCodificado =("VVJKQ3tTTTRMTF9CNFMzXzY0fQ==")

decodificado = base64.b64decode(textoCodificado)

print(decodificado)
print(decodificado.decode("UTF-8"))