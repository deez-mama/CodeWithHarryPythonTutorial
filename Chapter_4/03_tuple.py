#Tuple is immutable

a=(1,2,5,6)

print(type(a))
a=(1)

print(type(a)) #This is interpreted as an integer

a=(1,)

print(type(a)) #This is interpreted as a tuple with one member

# a[0]=5 doesn't work as tuples are immutable 