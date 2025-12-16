# Write a program to print multiplication table of n using for loops in reversed order.

n=int(input("Enter a number to print its multiplication table in reversed order:"))
for i in range(10,-1,-1):
    print(f"{n} X {i} = {n*i}")


