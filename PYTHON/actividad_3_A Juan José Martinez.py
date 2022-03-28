print("Bienvenido a la calculadora de diviciones exactas")

num_1 = int(input("Para comenzar ingresá el numero que deseas dividir "))
num_2 = int(input("Ahora ingresa el dividendo "))

if  num_1 % num_2 == 0 :
    print("Esta es una DIVISIÓN EXACTA")
else:
    print("Esta NO es una DIVISIÓN EXACTA")
    
print("Gracias por utilizar nuestra calculadora!")