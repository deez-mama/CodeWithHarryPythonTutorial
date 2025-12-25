class Employee:
    language="Python" #This is class attribute
    salary=200000

Bishowjeet=Employee()
Bishowjeet.name="Bishowjeet" #This is an instance / object attribute

print(Bishowjeet.name,Bishowjeet.language)

Raju=Employee()
Raju.name="Raju"
print(Raju.name,Raju.language,Raju.salary)

#Here name is instance attribute and salary and language are class atributes as they directly belong to the class
