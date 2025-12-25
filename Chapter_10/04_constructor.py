class Employee:
    language="Python" #This is class attribute
    salary=200000

    def __init__(self,language,name,salary): #dunder method which is automatically called
        self.language=language
        self.name=name
        self.salary=salary
        print("I am creating an object")
        pass


    @staticmethod #makes the function below this a static method. Meaning that it doesn't need an obhect to be passe.
    def About_user(): #we dont need self here
        print("This gives you information about the user: ")

Bishowjeet=Employee("Javascript","Bishowjeet",2100000)

Bishowjeet.About_user()

print(Bishowjeet.name,Bishowjeet.language,Bishowjeet.salary)