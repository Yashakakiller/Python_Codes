# __str__ and super()
class Student:
    def __init__(self,name):
        self.fullName = name 

    def displayName(self):
        print(f"{self.fullName}")

    def __str__(self):
        return f"This side {self.fullName}"


class Programmer(Student):
    def __init__(self,name,port):
        super().__init__(name)
        self.port = port 

    def displayName(self):
        print(f"Hello {self.fullName}")

    # def displayName(self): #this will override the above method
        # return super().displayName()

    def greetProgrammer(self):
        print(f"Hey PROGRAMMER {self.fullName} .... Your Localhost is running on Port {self.port}")

    def __str__(self):
        return f"{self.fullName} this side"
    
    # def __str__(self):
    #     return super().__str__()


yash = Programmer(name="Yash Gupta",port=8080)
# yash.greetProgrammer()
# yash.displayName()

rachit = Student(name="Rachit Laddha")
# rachit.displayName()
# rachit.greetProgrammer() >> this will raise error 

print(rachit)
print(yash)