#floor Division
num1= 5//2
print(num1) # whole number after 5/ by 2 

# modules
num2= 5%2
print(num2)

# power of
a=2
b=3
 
d= a**2
e= a**b
print(d) 
print(e)

#identity operators------------
#(is, is not)
#      x-----> [10]  
#      y-----> [10]  x is y ==> ture
#                    x is z ==> false
#      z-----> [8]
#                    x is not y ==> false
#                    x is not z ==> true

x= 10
y=10
z=8

print(x is y) # check the value of memory address
print(x is not y)

# print the id(memory address) of a variable.
print(id(x)) # same id
print(id(y)) # same id
print(id(z)) # different id 