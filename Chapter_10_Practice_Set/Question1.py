# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
        pass
        
p=Programmer("Bishowjeet",2000000,676767)
r=Programmer("Harry",2000000,676767)
print(p.name,p.salary,p.pin,p.company)
print(r.name,r.salary,r.pin,r.company)