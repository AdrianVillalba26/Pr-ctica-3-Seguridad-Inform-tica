#pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

clave = b'SeguridadInforma'  
iv = b'SeguridadInforma'   

def cifrar(texto_plano):
    cipher = AES.new(clave, AES.MODE_CBC, iv)
    texto_plano = pad(texto_plano.encode(), AES.block_size)
    texto_cifrado = cipher.encrypt(texto_plano)
    return binascii.hexlify(texto_cifrado).decode()

def descifrar(texto_cifrado_hex):
    texto_cifrado = binascii.unhexlify(texto_cifrado_hex)    
    cipher = AES.new(clave, AES.MODE_CBC, iv)
    texto_plano = unpad(cipher.decrypt(texto_cifrado), AES.block_size)
    
    return texto_plano.decode()

texto_plano = cifrar("hola_mundo")
texto_cifrado_hex = "F55228945ACF1A291DB0C84409852406"
print(f"Texto Cifrado (Hex): {texto_plano}")

texto_descifrado = descifrar(texto_cifrado_hex)
print(f"Texto Descifrado: {texto_descifrado}")

