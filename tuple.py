tpl1=(10,20,30,40,50)

# also we can crete tuple by inbuilt function
tpl2=tuple() 

print(type(tpl2))

print(tpl1)
print(tpl1[1])
# immutable so we cant change the value
tpl1[0]=1
print(tpl1) # this output will show you error