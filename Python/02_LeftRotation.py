
import numpy as np

entrada = input().strip().split(" ")
tam_list = int(entrada[0])
rotacion = int(entrada[1])
#print("Tam lista: ",tam_list,"\nRotacion: ",rotacion)
lista = input().split(" ")
#print(lista)
for i in range(rotacion):
    lista.append(lista.pop(0))
    #print(lista[:])

for i in lista:
    print(i,end=" ")