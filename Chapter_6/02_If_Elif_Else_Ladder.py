age=int(input("Enter your age: "))

#If-elif-else ladder

if(age>18):
    print("You are above the age of consent")

elif(age<=0):
    print("Age is invalid")

else:
    print("You are below the age of consent")

print("End of program")