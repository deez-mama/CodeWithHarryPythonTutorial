# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

from random import randint #allows direct use of randint instead of random.randint

class Train:

    def __init__(self,trainNo,fro,to):
        self.trainNo=trainNo
        self.fro=fro
        self.to=to

    def book(self):
        print(f"The train is booked in number {self.trainNo} from {self.fro} to {self.to}")
        
    def status(self):
        print(f"The train {self.trainNo} is succesfully driving from {self.fro} to {self.to}")
    def getFare(self):
        print(f"The train-fare of train number: {self.trainNo} from {self.fro} to {self.to} is {randint(50,500)}") #we don't need random.randint cause we imported from random


a=Train(67,"Kathmandu","Pokhara")
a.getFare()
a.book()
a.status()
