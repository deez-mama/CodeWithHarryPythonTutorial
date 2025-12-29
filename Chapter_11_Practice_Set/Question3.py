# Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.

class Employee:
    def __init__(self,salary,increment):
        self.salary=salary
        self.increment=increment
    
    @property
    def salaryAfterIncrement(self):
        return f"Your new salary is {self.salary+self.salary*(self.increment/100)}"

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self):
        self.salary=self.salary+self.salary*(self.increment/100)


salary=int(input("Enter your salary : "))
increment=int(input("How much percent increment in salary do you need? : "))

s=Employee(salary,increment)
print(s.salaryAfterIncrement)


