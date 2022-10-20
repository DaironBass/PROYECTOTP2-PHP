"""¿Cuál es la sintaxis correcta para crear una clase denominada 
que heredará propiedades y métodos de una clase denominada ?StudentPerson"""
class Student(Person):


"""Hemos utilizado la clase para crear un objeto llamado .Studentx

¿Cuál es la sintaxis correcta para ejecutar el método del objeto?printnamex """
class Person:
    def __init__(self, fname):
        self.firstname = fname

    def printname(self):
        print(self.firstname)

class Student(Person):
    pass

x = Student("Mike")
x.printname()


