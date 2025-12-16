# Write a program to find whether a given number is prime or not.
num = int(input("Enter a number to check if it is prime or not: "))

i=1
count=0

while(i<=num):
    if(num%i==0):
        count+=1
    i+=1

if(count==2):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")