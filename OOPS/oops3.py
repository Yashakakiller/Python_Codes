from oops import Teacher
class Employee:

    organisationName = "JECRC"
    
    def __init__(self,name,salary) :
        self.name = name 
        self.salary = salary

        print(self.name , self.salary)

    @classmethod
    def handleString(cls,string):
        return cls(string.split("__")[0],string.split("__")[1])

    def __str__(self):
        return (f" Name is {self.name} and salary is {self.salary}")

    def __call__(self,x):
        return self.name * x 




class Intern(Employee):
    def __init__(self,name,salary):
        return super().__init__(name,salary) #super() will refer the parent class
    

i1 = Intern("name",100)

# e = Employee("yash",1000000)
# et1 = e(5)
# print(et1)
# print(e)
# e_data = "akshat__100000000"
# e1 = Employee.handleString(e_data)
# print(e1)   


# print(dir(et1))  #this will print all the methods and functions of et1 


# print(e.__dict__)#this will show all the instance variables in object format


# print(help(type(e)))




t = Teacher()
print(t)


