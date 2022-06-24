import numpy as np 
a = np .array([1,2,3,4,5])
b = np.array([1,2,3,4,5])
print(a-b)
print(a+b)
print(a*b)
print(a/b)
print("_________________________")
print(a-1)
print(a+2)
print(a*3)
print(a/4)

print("_____________________________________________")

print( " matrix multiplication operatpr is '@'",a@b)
print( " matrix multiplication operatpr is 'a.dot(b)'",a.dot(b))
print("_____________________________________________")

rg = np.random.default_rng(1) 
rr = np.random .default_rng(2)
print(rg)
print(rr)



a = np.ones((2,3) ,dtype=int)
b= rg.random((2,3))
print(a)
print(b)

print("the max value of b",b.max())
print("the min value of b is ",b.min())
#print("the min value of b is ",b.min(axis=3))
#print("the max value of b",b.max(axis = 2))#
print("the sum of the a,b is ",np.add(a,b))
print("the sum of the a,b is ",a+b)
from numpy import pi
b = np.linspace(9, pi, 3)
print(b)

