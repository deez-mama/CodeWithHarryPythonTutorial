class apple:
    a=1

    @classmethod 
    def show(cls): 
        print(f"The class value of a is {cls.a}") #This prints "1" because of @classmethod
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e=apple()
e.a=45 #Object attribute overrides class attribute

e.name="Bishowjeet Bhandari" 
print(e.name)
print(e.fname,e.lname)
e.show()


