a=15

def something():
    a=10
    globals()['a']=9
    print("in func", a)

something()

print("out side ", a)