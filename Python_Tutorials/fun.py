def add(x,y):
    c=x+y
    return c

result=add(2,3)
print(result)                          #Actual arguments
                                              #  position
                                              # keyword
                                              #Default
def person(name, age=18):      #default arguments                   #varaible length
      print(age)
      print(name)

#person(age= 39,name ='rajani')  # key word arguments

person('vasisht')


def add1(*b):  # variable length arguments
    c=0
    for i in b:
        c=c+i
    print(c)

res=add1(2,5,4, 5,6)
print(res)


#keyword length arguments

def person(name, **data):
    for i,j in data.items():
        print(i,j)
        print(name)


person("rajani", age=39, place="Mckinney")