class Employee:
    company="Meta"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
    
class comp(Employee):
    company="Leapfrog"

    def Language(self):
        print(f"THe person {self.name} is good with {self.language}")

a=Employee()
b=comp()

print(a.company,b.company)
