class Student:

    instituteName = "JECRC UNIVERSITY" #class variable

    def __init__(self,name,age,email,location):#self represents the object
        print("you have initialised a constructor") 

        #these are the instance variables
        self.name = name   
        self.age =age    
        self.location = location  
        self.email = email    


    #access specifiers in variables and functions

        self.public_var = "I'm Public "
        self._protected_var = "I'm Protected "
        self.__private_var = "I'm Private "

    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method") 



    
    def __str__(self):
        return ("You have called the object")
    
    def showDetails(self): #this is a class method
        print(f"Your name is {self.name} , age is {self.age} , location is {self.location} and email is {self.email}. \n The institute name is {self.instituteName}")

    @classmethod
    def showInstituteName(cls):
        print(cls.instituteName)

    @staticmethod
    def greet():  #this is a static method , called by any object or without object
        print("Hello Everyone")




p2 = Student(name="Akshat Jain",email="akain@gmail.com",age=18,location="Bangkok")

p1 = Student(name="Yash Gupta" ,email="yashakakiller@gmail.com", location="Jaipur",age = 18) #this will call the constructor
p1.instituteName = "Poornima University" #this will create a new instace variable and not change the class variable
p1.showDetails()
# print(Student.instituteName)
# Student.showInstituteName()
# print(p2.__dir__())

# print(p2)


#working with access speicifiers
print(p1.public_var)
p1.public_method()

# Protected attributes and methods can be accessed (but it's a convention not to)
print(p1._protected_var)  
p1._protected_method()   

#The name mangling convention in Python is to add a double underscore (__) prefix to attribute and method names that are intended to be private. When you use double underscores to prefix a variable or method name, Python will internally modify the name to include the class name as a prefix, making it harder to accidentally override in subclasses.
print(p1._Student__private_var)





#use this class in another module
class Teacher:
    name = "Harry"

#magic methods and dunder methods
    def __init__(self):
        print("created a object")

    def __len__(self):
        return len(self.name)
    
    def __call__(self):
        return "object calling "

    def __str__(self):
        return "calling a class object"
    
