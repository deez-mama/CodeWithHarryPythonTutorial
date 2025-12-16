# Write a program to print multiplication table of a given number using for loop.

num=int(input("Enter a number to print its multiplcation table:"))

for i in range(11):
    print(f"{i} X {num} = {i*num}")

