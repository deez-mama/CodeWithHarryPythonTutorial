#Write a program which finds out whether a given name is present in a list or not.

names_list=["Alice", "Bob", "Charlie", "David", "Eva"]

name=input("Enter a name to search: ")

if(name in names_list):
    print("The name is present in the list")

else:
    print("The name is not present in the list")