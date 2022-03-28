
#segundo programa

num_1 = int(input("Ingrese el primer numero "))
num_2 = int(input("Ingrese el segundo numero "))
num_3 = int(input("Ingrese el tercer numero "))

if num_1 == num_2 == num_3 :
    print("Son todos iguales")
elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3 :
    print("Dos de los numeros que ingresaste son iguales")    
else: 
    print("Son todos distintos")
