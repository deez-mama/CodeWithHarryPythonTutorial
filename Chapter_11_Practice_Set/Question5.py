#Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.


class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self,other):
        res=vector(self.x+other.x,self.y+other.y,self.z+other.z)
        return res

    def __mul__(self,other):
        res= self.x*other.x+self.y+other.y+self.z*other.z
        return res
    
    def __str__(self):
        return f"{self.x},{self.y},{self.z}"

v1=vector(2,5,1)
v2=vector(4,3,2)
v3=vector(2,3,1)

print(v1+v2)
print(v1*v2)
print(v1+v3)
print(v1*v3)
