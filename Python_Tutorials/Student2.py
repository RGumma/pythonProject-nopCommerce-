class Student2:

    def __init__(self,m1, m2):
        self.m1=m1
        self.m2=m2

    def add(self,a=None,b=None,c=None):
         s=0
         if a!=None and b!=None and c!=None:
            s= a+b+c
         elif a!=None or b!=None:
            s= a+b
         else:
            s=a

            return s

s=Student2(1,2)

result=s.add(10,20)
print(result)
