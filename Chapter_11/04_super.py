#super is used when we need all the contructors of different hierarchial classes to run

class Employee:
    def __init__(self):
        print("Constructor of Employee is called")
    a=1


class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer is called")
    b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager is called")
    c=3

o=Manager()

print(o.a)

