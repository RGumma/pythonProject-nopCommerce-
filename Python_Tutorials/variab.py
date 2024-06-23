import math
from array import *

x,y,z=10,20,30
print(x,y,z)

x=y=z=10
print(x,y,z)

x=int(20)
print(type(x))

a=5; b=6
x=bool(0)
print(x)


i=a>b
print(i)

y=range(1,10)
print(y)
y=list(range(1,10))

print(y)

x=math.sqrt(25)
print(x)

z=math.floor(2.9)
print(z)

#a= float(input("Enter  a number"))
#b= float(input("Enter a number "))

z= a+b
print(z)




vals = array('i',[2,-3,4,5])
print(vals)


#for i in range(len(vals)):
    #print(vals[i])

arr= array('i',[])

n = int(input("Enter the length of the array"))

for i in range(n):
    x=int(input("Enter the elements"))
    arr.append(x)
print(arr)

n=int(input("Enter the value to search"))

k=0
for e in arr:
    if e==n:
        k=k+1;
        break
print(k)



















































































































































































































































































