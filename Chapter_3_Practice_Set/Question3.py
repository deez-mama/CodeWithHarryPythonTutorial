#Write a program to detect double space in a string.
string=input("Enter a string: ")

check=string.find("  ")

print("Presence of double space: ",check>1)