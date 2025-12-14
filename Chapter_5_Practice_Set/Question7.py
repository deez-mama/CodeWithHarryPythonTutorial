# If the names of 2 friends are same; what will happen to the program in problem 6?

my_dict={}

v1=input("Enter your favorite language, friend 1: ")
v2=input("Enter your favorite language, friend 2: ")
v3=input("Enter your favorite language, friend 3: ")
v4=input("Enter your favorite language, friend 4: ")
my_dict.update({"friend 1":v1, "friend2":v2, "friend 3":v3, "friend 4":v4})

print(my_dict)

print("If the names of 2 friends are the same, the last entry will overwrite the previous one for that name, resulting in only one entry for that name in the dictionary.")