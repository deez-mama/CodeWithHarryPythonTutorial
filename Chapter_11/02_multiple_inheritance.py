class Employee:
    company="Meta"
    name="Bishowjeet"
    salary=2000000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
    

class code():
    language="Python"
    def lang(self):
        print(f"Your language is {self.language}")  

class comp(Employee,code):
    company="Leapfrog"

    def Language(self):
        print(f"THe person {self.name} is good with {self.language}")

a=Employee()
b=comp()

b.show()
b.Language()
b.lang()

