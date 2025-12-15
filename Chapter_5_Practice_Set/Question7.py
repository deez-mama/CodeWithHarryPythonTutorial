# If the names of 2 friends are same; what will happen to the program in problem 6?


my_dict={}


name=input("Enter friend's name: ")
language=input("Enter favorite language: ")
my_dict.update({name:language})

name=input("Enter friend's name: ")
language=input("Enter favorite language: ")
my_dict.update({name:language})

name=input("Enter friend's name: ")
language=input("Enter favorite language: ")
my_dict.update({name:language})

name=input("Enter friend's name: ")
language=input("Enter favorite language: ")
my_dict.update({name:language})

print(my_dict)


print("If the names of 2 friends are the same, the last entry will overwrite the previous one for that name, resulting in only one entry for that name in the dictionary.")