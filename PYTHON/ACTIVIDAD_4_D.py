#4) Escribí un programa que pida al usuario cuantos números quiere introducir.
#  Luego lee todos los números y realiza una media aritmética:

suma_total = 0
print("Vamos a calcular la media de todos los números que ingreses ")
cantidad_de_numeros = int(input("Cuantos números queres calcular?"))
for numeros in range (cantidad_de_numeros):
    suma_total += float(input("Ingresá un número "))
media_total = suma_total/cantidad_de_numeros
print ("La media es ",media_total)