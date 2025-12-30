# method to print the vector as follows:
#  7i + 8j +10k 
# Assume vector of dimension 3 for this problem.

class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __str__(self):
        return(f"{self.x}i + {self.y}j + {self.z}k")

x=7
y=8
z=10

vec=Vector(x,y,z)
print(vec)
