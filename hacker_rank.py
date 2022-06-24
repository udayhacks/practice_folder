"""
problem of the  finding the sum of 4 of 5 whose sum is min and max of it 
-
"""




def u(l):
    
    a = min(l)
    b = max(l)
    s = sum (l)
    mn = s-b
    mx = s-a
    return mn ,mx

l = [1,2,3,4,5]
print(u(l))