#Recorra los elementos de la lista.fruits

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#En el bucle, cuando el valor del elemento es "banana", vaya directamente al siguiente elemento.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":   
        continue
    print(x) 

#Utilice la función para recorrer un conjunto de códigos 6 veces.range
for x in range(6):
    print(x)


#Salga del bucle cuando sea "banana".x
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


    
