#oops => Object Oriented Programming
class Student:
    def __init__(self):
        print("you have created a student")
    

    def getValues(self,fullName,age,email):
        self.name = fullName
        self.age = age 
        self.email = email 
    
    def showValues(self):
        print("Your name is {self.}")