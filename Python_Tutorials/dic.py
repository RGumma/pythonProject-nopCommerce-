thisdict ={ 'brand': 'Ford', 'model': 'Mustang','year':1956}
print(thisdict)


for x in thisdict.keys():
    print(x)

for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
    print(x,y)

thisdict.update({'price': 100000})
print(thisdict)

# which is ordered , changeable and does not allow duplicates

y=thisdict.get('brand')
print(y)

z=thisdict.keys();
print(z)

thisdict.pop('year')

y=thisdict.values()
print(y)