# Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects

class Employee:
    def __init__(slf,name):
        slf.name=name

    def prr(harry):
        print(f"The name is {harry.name}")


a=Employee("Bishowjeet")

a.prr()

#Yes, replacing self with other strings is possible but its not a good practice and it brings redability issues.