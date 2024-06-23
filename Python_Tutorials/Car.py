class Car:
    wheels=4                 #class namespace
    def __init__(self):
        self.mil=10         #instance namespace
        self.com="BMW"

Car.wheels=5


c1=Car()
c2=Car()
c1.mil=15
print(c1.mil, c1.com, Car.wheels)
print(c2.com, c2.mil,Car.wheels)

