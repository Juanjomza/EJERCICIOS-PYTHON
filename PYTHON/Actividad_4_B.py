# Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar,
#  debe repetirse el proceso hasta que lo introduzca correctamente.

#Inicializo la variable en 0

num1 = 0
while num1 % 2 == 0: #mientras el "resto" de la division sea cero se que el número ingresado no cumple con la condicion
    num1 = int (input("Ingrese un numero impar "))