from functools import reduce
def check_len(lst):
    count=0
    for i in lst:
        if len(i)>5:
            count=count+1
    return count

lst=['rajani', 'ravi', 'kota', 'vasisht', 'vedardh','prabhavathi']
count=check_len(lst)
print(count)

f=lambda a : a*a
result = f(5)
print(result)

def is_even(n):
    return n%2==0

nums=[2,3,5,6,7,8]

evens = list(filter(is_even,nums))
evens1 = list(filter(lambda n:n%2==0,nums))#using lambda
doubles = list(map(lambda n:n*2,nums))
print(doubles)
sum = reduce(lambda a,b:a+b,doubles)

print(sum)

print(evens)

evens