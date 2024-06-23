from numpy import *



                                          # create the arrays in different ways
arr1  = array([1,2,4,7])                        #array()
                                                 #linspace()
print(arr1)                                        #logspace()
                                            #arange()
arr= arange(1,20,2)
print(arr)
                                                        #zeros()
arr = zeros(5, int)                                 #ones
print(arr)

arr =linspace(1,40,5)
print(arr)
arr= logspace(1,40,2)

arr = array([2,4,5,6])
print(arr+5)
print(arr[0]+arr[2])

arr = array([[1,2,3],[4,5,6]])

print(arr[0,0])

print(arr[0,1:2])

arr1= array([1,2,3])
arr4=arr1.view()                 #shallow copy
print(id(arr1))
print(id(arr4))                #deep copy
print(arr4)
print(arr1)
arr2= array([4,5,6])
arr3= arr1+arr2
print(arr3)
print(sum(arr1))
print(min(arr1))
print(concatenate([arr1,arr2]))

arr=array([[8,9,10],[5,6,7]])
arr2=arr.flatten()
print(arr2)


print(arr.ndim)
print(arr.shape)
print(arr.size)

m= matrix('1 2 3 ; 6 4 5; 1 6 7')
print(m)
