class Computer:

    brandName = "Yash_Wheels"  # class variables;

    #constructor
    def __init__(self,ram,processor): # ram and processors are instance variables
        self.ram = ram 
        self.processor = processor
        # print("You had initialised new computer")

        self.gamingPC = self.GamingComputer()


    #methods
    def showConfig(self):
        print(f"The configurations are {self.processor}")


    def compare(self,otherComputer):
        if(self.ram == otherComputer.ram) :
            return True 
        else:
            return False
    

    #class methods
    @classmethod  #decorators
    def info(cls):
        print("BrandName is",cls.brandName)
        

    #static methods
    @staticmethod
    def greet():
        print("Hello Static Users")



    class GamingComputer:
        def __init__(self):
            self.brandName = "Asus"
            self.computerSeries = "TUF Gaming"
            self.processor = "Ryzen 7 7700H"
            self.ram = 16

        def showConfig(self):
            print(f"The processor is {self.processor} , it has {self.ram} ram and the brand name and series is {self.brandName} {self.computerSeries}")






com1 = Computer(ram=8 ,processor="ryzen 5 5500u")
com2 = Computer(ram=16,processor="ryzen 5 5600h")

com1.showConfig()   #Computer.config(com1)

'''if com1.compare(com2):
    print("They are having same ram configuration")
else:
    print("Don't have same ram configurations")'''

com1.processor = "i7 13Gen"
# com1.brandName = "New_Car_Company"

Computer.brandName = "Tech_Wheels"

print(com2.ram, com1.processor)
print(com1.brandName, com2.brandName)

Computer.info()

Computer.greet()


print(com1.gamingPC.computerSeries)

com3 = Computer(ram=8,processor="ryzen 5 4600H")
gc1 = com3.gamingPC
print(gc1.processor)

gc2 = Computer.GamingComputer()
gc2.showConfig()