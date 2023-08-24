#oops

class Student:
    #constructor
    def __init__(self,name,email,age,phone,address):
        self.name = name
        self.age = age 
        self.email = email 
        self.phone = phone 
        self.address = address
    '''
      name  = ""
     email = ""
     age = 0
     phone = 0
     address = "" 
     '''

    def info(self):
        print(f"Hello {self.name} ! You have registered in our school with {self.email} and {self.phone} .. Your age is {self.age} and your address is {self.address}")


yash = Student("Yash Gupta","yashakakiller@gmail.com",18,9928585137,"Jaipur")
'''
yash.name = "Yash Gupta"
yash.address = "Jaipur"
yash.age = 18
yash.phone = 9928585137
yash.email = "yashakakiller@gmail.com"
'''

# yash.info()



#decorators

def welcome(function):
    def wrapper():
        print("Before calling the passed function")
        function()
        print("After calling the passed function")
    return wrapper


# @welcome
# def greet():
#     print("Hello World")

# greet()


def greet():
    print("Hello World")

# welcome(greet)()





# Example 2: Decorator with arguments

def times(num):
    def decorator(func):
        def wrapper(*args):
            for i in range(num):
                result = func(*args)
            return result
        return wrapper
    return decorator

@times(num = 5)
def greet(fname,lname):
    print("Hello",fname , lname)

# greet("yash","gupta")






