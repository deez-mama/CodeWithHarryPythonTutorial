# Write a program to calculate the factorial of a given number using for loop.

num=int(input("Enter a number to find its factorial: "))

factorial=1

for i in range(1,num+1):
    factorial=factorial*i

print(f"The factorial of {num} is {factorial}.")
