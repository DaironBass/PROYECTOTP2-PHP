#Compruebe si "manzana" está presente en el conjunto.fruits
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

#Utilice el método para agregar "orange" al conjunto.addfruits
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Utilice el método correcto para agregar varios elementos () al conjunto.more_fruitsfruits
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)


#Utilice el método para eliminar "banana" del conjunto.removefruits
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")


#Utilice el método para eliminar "plátano" del conjunto.discardfruits
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")



