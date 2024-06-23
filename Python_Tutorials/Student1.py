class Student1:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1= self.m1+other.m1
        m2= self.m2+other.m2
        s3=Student1(m1,m2)         #operator overloading
        return s3

    def __gt__(self, other):
        r1=self.m1+other.m1
        r2=self.m2+other.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self):
        return self.m1, self.m2

s1 = Student1(45,67)
s2 = Student1(82,56)

s3=s1+s2
print(s3.m1)
print(s3.m2)
if(s1>s2):
    print("s1 wins")
else:
    print("s2wins")

print(s1.__str__())
