age=int(input("Enter your age: "))

#If statemen no.1

if(age%2==0):
    print("The number is even")

#If statement no.2

if(age>18):
    print("You are above the age of consent")

elif(age<=0):
    print("Age is invalid")

else:
    print("You are below the age of consent")

print("End of program")