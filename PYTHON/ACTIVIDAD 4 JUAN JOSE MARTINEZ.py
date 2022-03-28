#1) Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
#Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números
#Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
#En caso de no introducir una opción válida, el programa informará de que no es correcta.

print("Bienvenido a tu calculadora!")
num1 = float (input("Para comenzar ingresa el primer numero de la operación: "))
num2 = float (input("Ahora ingresá el segundo numero de la operación: "))
option = 0
print ("Que operación deseas realizar? \n1) Si deseas sumarlos \n2)Si deseas restarlos \n3)Si lo que quieres hacer es multiplicar"),
option == int (input("Introduce la opcion: ")),
if option == 1:
    print( "El resultado es de la suma de " (num1 + num2) ),
elif option == 2:
    print("El resultado de la resta de " (num1 - num2) ),
elif option == 3:
    print("el resultado de la multiplicadio "(num1 * num2) ),
else:
    print("Opcion incorrecta")

