#fstrings

letter = "Hey my name is {1} and I am from {0}"

country  = "India"
name = "YASH"

newLetter = f"Hey my name is {name} and I am from {country}"

# print(newLetter,"\n")
# print(letter.format(country, name))


# txt = "For only {price:.4f}"
# print(txt.format(price = 20.2334534))

# price = 20.2334534
# txt = f"only for {price:.2f}"
# print(txt)

a = f"hi {{name}} hi" #this will not populate name variable
# print(a)







#Docstrings 

#description of a function and it is not ignored by the interpreter

#also it is written next to the line of the function declaration other wise the interpreter treat the docString as none

def square(n):
    '''
    This is an function which will print the square of a given number
    '''
    print(n * n)

square(9)
# print(square.__doc__)





