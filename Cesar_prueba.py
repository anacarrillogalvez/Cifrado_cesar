alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cifrado = "Si Cupdmzaplil Uikpwuis Icbwuwti lm Tmfpkw oi lmamtxmvilw cu xixms xzwbiñwupkw mu si opabwzpi g mu si nwztikpwu lm ucmabzw xipa. Sia bizmia acabiubpdia lm mabi puabpbckpwu xcjspki, icbwuwti g sipki awu si lwkmukpi, si pudmabpñikpwu g si lpncapwu lm si kcsbczi"

for clave in range (1, len (alfabeto)):
    mensaje = " "

    for letra in cifrado.upper (): 
        if letra in alfabeto:
            indice = alfabeto.find(letra)
            indice -= clave

        if indice < 0:
            indice += 27

        mensaje += alfabeto[indice]

    else:
        mensaje += letra

print (f"Clave: (clave) {mensaje}")