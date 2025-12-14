#Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

my_dict={}

v1=input("Enter your favorite language, friend 1: ")
v2=input("Enter your favorite language, friend 2: ")
v3=input("Enter your favorite language, friend 3: ")
v4=input("Enter your favorite language, friend 4: ")
my_dict.update({"friend 1":v1, "friend2":v2, "friend 3":v3, "friend 4":v4})

print(my_dict)
