#Single Inheritance
'''
class Parent:
    def func1(self):
        print("This function is in parent class.")
 
# Derived class
 
 
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
 
 
# Driver's code
object = Child()
object.func1()
object.func2()
'''


#multiple inheritance  (2 Parent Class >> 1 Child Class)
'''

class Mother:
    def __init__(self,name):
        self.mName = name
    
    def mother(self):
        print(f"Mother Name {self.mName}")


class Father:
    def __init__(self,name):
        self.fName = name
    
    def father(self):
        print(f"Father Name {self.fName}")


class Son(Mother,Father):
    def __init__(self,name,mName,fName):
        Mother.__init__(self,name=mName)
        Father.__init__(self,name=fName)
        self.name = name

    def showDetails(self):
        print(f"My name is {self.name} . My Mother name is {self.mName} and Father name is {self.fName}")


s1 = Son(name="Yash",mName="Meenu",fName="Mahadev")

'''


#multilevel Inheritance (Nani > Mummy > Son)
'''
class Nani:
    def __init__(self,name):
        self.nName = name

class Mother(Nani):
    def __init__(self,nName, mName):
        super().__init__(nName)
        self.mName = mName

class Son(Mother):
    def __init__(self,nName,mNmae,sName):
        super().__init__(nName ,mNmae)
        self.sName = sName
    
    def showInfo(self):
        print(f"My name is {self.sName} , my mother name is {self.mName} and my Nani name is {self.nName}")


obj = Son(nName="Mata Santosh",mNmae="Mata Meenu" ,sName="Yash")
obj.showInfo()

'''


#Hierarchical Inheritance
'''
# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class1


class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")

# Derivied class2


class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")


# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

'''



#Hybrid Inheritance (Combination of multiple inheritance)
'''
class School:
	def func1(self):
		print("This function is in school.")


class Student1(School):
	def func2(self):
		print("This function is in student 1. ")


class Student2(School):
	def func3(self):
		print("This function is in student 2.")


class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()
object.func2()
object.func4()

'''

