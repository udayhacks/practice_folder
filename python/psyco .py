l= [1,2,3,4,5]
i = [1,2,3,4,5]
for j  in enumerate(l,start = 2):
    
    print(j)
    
o =[ 
    (1,'q'),(2,'w'),(3,'e'),(4,'r')
    ]



p , u = zip(*o)
print(p,u)

print(2//2*2)
print(12*3//12)
print(12//3*12//4-2)




count = 0
while (count < 1):    
    count = count+1
    print(count)
    break
else:
    print("No Break")
    
    

# Function to convert number into string
# Switcher is dictionary data type here
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
 
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")
 
# Driver program
if __name__ == "__main__":
    argument=9
    print (numbers_to_strings(argument))
    
    
    
    
cars = ["Aston" , "Audi", "McLaren "]
cars = ["Aston" , "Audi", "McLaren "]
print( enumerate(cars))




import itertools as it
 
# defining the grouper function
def grouper(inputs, n, fillvalue = None):
    iters = [iter(inputs)] * n
    return it.zip_longest(*iters, fillvalue = fillvalue)
 
alpha = ['g', 'e', 'e', 'k', 's', 'f', 'o',
         'r', 'g', 'e', 'e', 'k', 's']
print(list(grouper(alpha, 4)))



