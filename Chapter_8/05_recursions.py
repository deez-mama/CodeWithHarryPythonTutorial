
n=int(input("Enter a number to find its factorial: "))



def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
a=factorial(n)
print(f"The factorial of {n} is {a}")
