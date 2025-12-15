#Write a program to find whether a given username contains less than 10 characters or not.

username=input("Enter your username: ")

count=len(username)

if(count<10):
    print("Username contains less than 10 characters")
elif(count==10):
    print("Username contains exactly 10 characters")
else:
    print("Username contains more than 10 characters")

