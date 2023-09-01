print("Ingresa el mensaje cifrado")
mensaje_cifrado = input()
print("Cuántas veces se movió la letra en el cifrado")
veces = int(input())

mensaje_descifrado = ""

for letra in mensaje_cifrado:
    minuscula = 'a' <= letra <= 'z'
    mayuscula = 'A' <= letra <= 'Z'
    if not (minuscula or mayuscula):
        mensaje_descifrado += letra
    else:
        ascii = ord(letra)
        base_ascii = ord('a')
        if mayuscula:
            base_ascii = ord('A')
        nuevo_ascii = (ascii - base_ascii - veces + 26) % 26 + base_ascii
        nueva_letra = chr(nuevo_ascii)
        mensaje_descifrado += nueva_letra

print("Mensaje descifrado:", mensaje_descifrado)