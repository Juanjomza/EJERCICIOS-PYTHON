#solicito el ingreso de las notas por pantalla
#nota_1= float (input ("Ingrese nota del primer examen "))
#nota_2= float (input ("Ingrese nota del segundo examen "))
#nota_final = (nota_1 * 0.4 + nota_2 * 0.6)
#print ("La nota final es " , nota_final)

#REORDENAR
# cadena_1 = "moderno."
 #cadena_2 = "Python"
#cadena_3 = "es un lenguaje"
#cadena_4 = "de programación"

#print (cadena_2, cadena_3, cadena_4, cadena_1)

#listagrande= [
#lista1 = [1, 12, 123,52] [25, 56, 85] 

#lista2 = ["Bye", "Ciao","Chau"


#matriz = [[1, 5, 1], [2, 1, 2], [3, 0, 1], [1, 4, 4]]

#matriz[0][len(matriz[0]):]= [sum(matriz[0])]

#matriz[1][len(matriz[1]):]= [sum(matriz[1])]

#matriz[2][len(matriz[2]):]= [sum(matriz[2])]

 #matriz[3][len(matriz[3]):]= [sum(matriz[3])]

#for a in range(len(matriz)):
 #   matriz[a].append(sum(matriz[a]))


#print(matriz)


num_1 = int(input("Ingrese el primer numero"))
num_2 = int(input("Ingrese el segundo numero"))
num_3 = int(input("Ingrese el tercer numero"))

if num_1 == num_2 == num_3 :
    print("Son todos iguales")
elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3 :
    print("Hay dos iguales")    
else: 
    print("Son todos distintos")
