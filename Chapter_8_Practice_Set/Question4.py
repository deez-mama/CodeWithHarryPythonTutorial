# Write a recursive function to calculate the sum of first n natural numbers.

def sum_natural_numbers(n):
    if n==1:
        return 1
    return n+sum_natural_numbers(n-1)

num=int(input("Enter a number: "))

print(f"The sum of first {num} natural numbers is {sum_natural_numbers(num)}")

