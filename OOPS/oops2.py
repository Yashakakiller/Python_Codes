''' 
         INHERITANCE
A -> B   (SINGLE-LEVEL)
A -> B -> C (MULTI-LEVEL)
A , B   -> C (MULTIPLE-LEVEL)
'''

class A:

    def __init__(self):
        print("You had initialsed a new object for class A")

    def feature1(self):
        print("Feature 1 working from A")

    def feature2(self):
        print("Feature 2 working")
    
    def execute(self):
        print("hey this is executing here")


#super keyword represents the parent class
class B:

    def __init__(self):
        print("You had initialsed a new Object for class B")

    def feature1(self):
        print("Feature 1 working from B")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


    def polyTest(self,classTest):
        classTest.execute()



class C(B,A):
    def __init__(self):
        print("You had initialsed a new Object for class C")
        super().__init__() #this will give more superiority to Left side class
        A.__init__(self)  # another way to use parent class

        



        
obj1 = B()
obj2 = A()

obj1.polyTest(obj2)

# obj1 = C()
# obj1.feature1()
