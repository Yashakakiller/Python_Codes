#exercise

# quesList = ['Who invented the Light Bulb?','Which planet in our solar system is known as the Red Planet?','What is the name of the biggest planet in our solar system?','Who invented the Telephone?','Which is the hottest planet in our solar system?']


# correctAnswers = ['Thomas Alva Edison','Mars','Jupiter','Alexander Graham Bell','Venus']

# totalPrice = 0
# for i in range(len(quesList)):
#     print(quesList[i])
#     userInput = input("Enter your answer : ").title()
#     if(userInput == correctAnswers[i]):
#         print("Yes, you are correct")
#         totalPrice+=100000
#     else:
#         print("OOPS, you are incorrect")
#         print("The correct answer is",correctAnswers[i])

# print("you had won total",totalPrice)






# a = input("Enter : ")
# try:
#     if(int(a)<0 or int(a)>9):
#         raise ValueError("invalid value")
# except:
#     if(a != "quit"):
#         raise TypeError("invalid value format")
    
# print("code run ")




# import random

# userMessage = input("Enter user Message ")
# randomChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# messageList= []
# for i in userMessage:
#     # print(i)
#     messageList.append(i)

# firstChar = messageList.pop(0)
# messageList.append(firstChar)

# for i in range(6):
#     if(i % 2 == 0):
#         randomC = random.choice(randomChar)
#         messageList.append(randomC)
#     else:
#         randomC = random.choice(randomChar)
#         messageList.insert(0, randomC)


# userMessage = ''.join(map(str, messageList))
# print(userMessage)





# class Library:

#     def __init__(self):
#         self.noOfBooks = 6
#         self.books = ["Python For Data Analysis","Automate The Boring Stuff With Python","Machine Learning with Python Cookbook","Python CookBook","Hands-On Machine Learning with Scikit-Learn and TensorFlow","Data Visualization in Python"]


#     def showBooks(self):
#         for i in self.books:
#             print(i)

#     def addBook(self,bookName):
#         self.noOfBooks+=1
#         self.books.append(bookName)

#     def showNoOfBooks(self):
#         print(len(self.books))

# lib1 = Library()
# lib1.showBooks()
# lib1.showNoOfBooks()
# lib1.addBook("Fluent Python: Clear, Concise, and Effective Programming, by Luciano Ramalho")
# print("\n\n")
# lib1.showBooks()
# lib1.showNoOfBooks()








# import os 

# fileContents = os.listdir("Waste_Materials")

# for index,file in enumerate(fileContents , start=0):
#     if(".txt" in file):
#         os.rename(f"Waste_Materials/{file}",f"Waste_Materials/style {index}.css")



