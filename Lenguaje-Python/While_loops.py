#Imprima siempre que sea inferior a 6.ii
i = 1 
while i < 6:
    print(i)
    i += 1

#Detenga el bucle si es 3.i    
i = 1

while i < 6:
  if i == 3:    
    break
  i += 1


#En el bucle, cuando es 3 , salta directamente a la siguiente iteración
i = 0
while i < 6:
    i += 1
    if i == 3:    
        continue
    print(i)


#Imprima un mensaje una vez que la condición sea false.  
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

