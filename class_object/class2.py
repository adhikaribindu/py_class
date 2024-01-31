class Vehicle:
    no_of_wheel=2 #attributes

class Car(Vehicle):
    no_of_wheel=4
    def get_wheel(self): #self
        return self.no_of_wheel
c1=Car().get_wheel()
print(c1)