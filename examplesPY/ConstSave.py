#!/usr/bin/python3

import pickle

class Person:
    
    def __init__(self, name, genero, edad):
        self.name = name
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona, con name: ", self.name)

    def __str__(self):
        return "{} {} {}".format(self.name, self.genero, self.edad)

class ListPerson:
   
    person = []

    def __init__(self):

        listofPerson = open("fichero", "ab+")
        listofPerson.seek(0)
        
        try:
            self.person = pickle.load(listofPerson)
            print("Se cargaron {} personas del fichero".format(len(self.person)))
        except:
            pass
        finally:
            listofPerson.close()
            del(listofPerson)

    def addPerson(self, p):
        self.person.append(p)
        self.savePerson()

    def showPerson(self):
        for p in self.person:
            print(p)

    def savePerson(self):
        listofperson = open("fichero", "wb")
        pickle.dump(self.person, listofperson)
        listofperson.close()
        del(listofperson)

    def showinfo(self):
        print("La informacion del fichero creado es:")
        for p in self.person:
            print(p)

mylist = ListPerson()
p = Person("Emmus", "Male", "18")
mylist.addPerson(p)
mylist.showinfo()

