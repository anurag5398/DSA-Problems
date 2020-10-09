
#SINGLETON
#__shared__ is a shared component for all instances
#MONOSTATE 
class Test:
    __shared = dict()
    def __init__(self, word):
        self.__dict__ = self.__shared
        self.state = word
    
    def __number(self, temp):
        return temp
    no = 2213

    def check(self):
        print(self.state)

p1 = Test("abc")
p2 = Test("xyz")

print(p1.state, p2.state)
print(p1._Test__shared)


#FACTORY
class CarType:
    def wheels(self):
        print("Has 4 wheels")

class BikeType:
    def wheels(self):
        print("Has 2 wheels")

class AutoType:
    def wheels(self):
        print("HAs 3 wheels")

def factory(vehicle = "Car"):
    types = {
        "Car" : CarType,
        "Bike" : BikeType,
        "Auto" : AutoType
    }

    return types[vehicle]()

car = "Car"
c = factory(car)
a = factory("Auto")
b = factory("Bike")

a.wheels()
b.wheels()


fn = "check"




