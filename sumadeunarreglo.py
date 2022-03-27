
#Suma de un arreglo
#Teniendo un arreglo de enteros encuentra el resultado de la suma de los elementos del arreglo. El arreglo debe de ser menor a mil datos.

lista = []

num = int(input("Introduce el numero de datos del array: "))
if num < 1000:

  print("Introduce los elementos del array: ")


for n in range(num):
  numbers = int(input())
  lista.append(numbers)
print("Suma:", sum(lista))
