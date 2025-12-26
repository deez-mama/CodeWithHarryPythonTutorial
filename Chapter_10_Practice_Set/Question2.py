# Write a class “Calculator” capable of finding square, cube and square root of a number.

n=int(input("Enter a number to find square, cube and square root: "))

class calculator:
    def __init__(self,n):
        self.num=n
        pass
    def square(self):
        print(f"The square of {self.num} is {self.num*self.num}")
    def cube(self):
        print(f"The cube of {self.num} is {self.num*self.num*self.num}")

    def square_root(self):
        print(f"The square root of {self.num} is {self.num ** 1/2}")

number=calculator(n)

number.square()
number.cube()
number.square_root()