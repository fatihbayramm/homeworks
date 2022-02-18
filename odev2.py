class Animal:
    def __init__(self, kind, name):
        self.kind = kind 
        self.name = name

class Cat(Animal):
    def meow(self):
        print("meow meow !")


class Cow(Animal):
    def moo(self):
        print("mooo !")


class Dog(Animal):
    def hav(self):
        print("hav hav !")

c = Cat("animal", "cat")
c.meow()
cw = Cow("animal", "cow")
cw.moo()
d = Dog("animal", "dog")
d.hav()

