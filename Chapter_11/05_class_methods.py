class apple:
    a=1

    @classmethod 
    def show(cls): 
        print(f"The class value of a is {cls.a}") #This prints "1" because of @classmethod

    def showAgain(self):
        print(f"The class value of a is {self.a}") #This prints "45" because instance attribute is able to override class attribute

e=apple()

e.a=45 #Object attribute overrides class attribute
e.show()
e.showAgain()



