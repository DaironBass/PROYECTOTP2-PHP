#Cree una función denominada .my_function
def my_function():
    print("Hello from a function")


#Ejecute una función denominada .my_function
def my_function():
    print("Hello from a function")
    my_function()


#Dentro de una función con dos parámetros, imprima el primer parámetro.    
def my_function(fname, lname):
    print(fname)


#Deje que la función devuelva el parámetro x + 5
def my_function(x):
    return x + 5


"""Si no conoce el número de argumentos que se pasarán a su función, 
hay un prefijo que puede agregar en la definición de la función, ¿qué prefijo?"""
def my_function(*kids):
    print("The youngest child is " + kids[2])


"""Si no conoce el número de argumentos de palabras clave que 
se pasarán a su función, hay un prefijo que puede agregar en la definición de la función, ¿qué prefijo?"""
def my_function(**kid):
    print("His last name is " + kid["lname"])










