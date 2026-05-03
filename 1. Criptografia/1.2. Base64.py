import base64
textoCodificado =("VVJKQ3tTTTRMTF9CNFMzXzY0fQ==")
textoSinCodificar = ("hola")

decodificado = base64.b64decode(textoCodificado)
datos_en_bytes = textoSinCodificar.encode("UTF-8")

codificado = base64.b64encode(datos_en_bytes)
texto_codificado = codificado.decode("UTF-8")

print(decodificado)
print(decodificado.decode("UTF-8"))
print(texto_codificado)
