marks=45
name= "dulhara"
if marks>=75:
    print("pass")
    print(": dulhara")
elif marks>65:
    print("B pass")
elif marks>55:
    print("C pass")

else: print("fail")

# formatted printing----------------

name,age,score="dulhara",22,45.5

print( "his name is :"+name+ " and he is :" +str(age)+" years old, his score is :"+str(score)) 

print( "his name is %s. and he is %d years old and his score is %0.2f" %(name,age,score))

print("his name is {}. and he is {} years old, his score is {}".format(name,age,score))
print("his name is {1}. and he is {0} years old, his score is {2}".format(name,age,score))

print(f"his name is {name}. and he is {age} years old. his score is {score}")

# getting user inputs--------------------
name=input("Enter your name :")
age=int(input("Enter your age :"))
score=float(input("Enter your score :"))

print(f"his new name is {name}")
print(f"his new age is {age}")
print(f"his new age is {score}")

print(type(name))
print(type(age))
print(type(score))

num1=int(input(" Enter num1 :"))
num2=int(input(" Enter num2 :"))
num3= num1+num2; 
print(num3)



