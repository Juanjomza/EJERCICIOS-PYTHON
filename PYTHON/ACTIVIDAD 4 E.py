#5) Escribí un programa que pida al usuario un número entero del 0 al 9, 
# y que mientras el número no sea correcto se repita el proceso. 
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo

numeros = [1, 3, 6, 9]
numero = int(input("Escribe un número del 0 al 9: "))
if numero >=0 and numero <=9:
    if numero in numeros:
        print("El número",numero,"se encuentra en la lista",numeros)
    else:
        print("El número",numero,"no se encuentra en la lista",numeros),

    print("Fin")       