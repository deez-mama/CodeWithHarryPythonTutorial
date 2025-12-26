# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class testing:
    a=60

obj1=testing()

print(obj1.a) #prints class attribute because there is no instance attribute

obj1.a=0 #Instance attribute is set.

print(obj1.a) # prints instance attribute because there it has been declared
print(testing.a) #Prints the class attribute.

#No, it does not change the class attribute

