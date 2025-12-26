class Employee:
    language="Python" #This is class attribute
    salary=200000

    @staticmethod #makes the function below this a static method. Meaning that it doesn't need an obhect to be passe.
    def About_user(): #we dont need self here
        print("This gives you information about the user: ")

    def getInfo(self): #Self is needed for all methods regardless of its use
        print(f"The language is {self.language} and salary is {self.salary}")

Bishowjeet=Employee()
Bishowjeet.language="Javascript" 

Bishowjeet.About_user()
Bishowjeet.getInfo()


#Another way to call this would be

#Employee.getInfo(Bishowjeet) -> This passes Bishowjeet and "self" accepts it




