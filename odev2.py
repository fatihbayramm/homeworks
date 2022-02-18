class Animal:

    def __init__(self, name):
        self.name = name
    
    def sound(self):
        raise NotImplementedError()

class Cat(Animal):
    def sound(self):
        print("meow meow !")


class Cow(Animal):
    def sound(self):
        print("mooo !")


class Dog(Animal):
    def sound(self):
        print("hav hav !")





c = Cat("animal")
c.sound()
cw = Cow("animal")
cw.sound()
d = Dog("animal")
d.sound()





