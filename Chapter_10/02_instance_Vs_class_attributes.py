class Employee:
    language="Python" #This is class attribute
    salary=200000

Bishowjeet=Employee()
Bishowjeet.language="Javascript" 

#Instance attribute takes priority over class attribute when seeting or getting data
#Hence the output becomes Javascript instead of python

print(Bishowjeet.language,Bishowjeet.salary)