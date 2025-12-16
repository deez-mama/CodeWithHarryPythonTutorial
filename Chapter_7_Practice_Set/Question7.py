"""
Write a program to print the following star pattern.
  *
 ***
***** for n = 3

"""

n=input("Enter the number of rows:")
n=int(n)

for i in range(n+1):
    print(" "*(n-i),end="")
    print("*"* (2*i-1),end="")
    print("")