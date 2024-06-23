class Inherit:

    def __init__(self):
        print("in 1 inherit")

    def feature1(self):
        print("In feature1")

    def feature2(self):
        print("In feature2")

#obj=Inherit()
#print(obj.feature1())
#print(obj.feature2())

class Inherit2(Inherit):

    def __init__(self):
        print("in 2 inherit")

    def feature3(self):
        print("in feature3")

    def feature4(self):
        print("in feature4")

#obj1=Inherit2()
#print(obj1.feature2())
#print(obj1.feature3())
#print(obj1.feature4())
#print(obj1.feature1())

class Inherit3(Inherit2, Inherit):

     def __init__(self):
        super().__init__()
        print("in 3 inherit")

     def feature5(self):
       print("in feature5")


obj3= Inherit3()                       #Method resolution order if we use c(A,B) preference is given to A
                                       #super method calls super class constructor