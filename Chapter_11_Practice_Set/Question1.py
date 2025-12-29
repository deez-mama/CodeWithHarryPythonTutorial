# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class two_D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show2(self):
        print(f"The 2-D vector is {self.x} i , {self.y} j")

class three_D(two_D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z=z
    def show3(self):
        print(f"The 3-D vector is {self.x} i , {self.y} j , {self.z} k")



x=int(input("Enter the x-componenent "))

y=int(input("Enter the y-componenent "))

z=int(input("Enter the z-componenent "))

b=three_D(x,y,z)

b.show2()
b.show3()



