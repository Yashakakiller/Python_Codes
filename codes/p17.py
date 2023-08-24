from functools import  reduce
#lambda

def square(x):
    return x**2

lsquare = lambda x : x**2

product = lambda x,y: x*y
# print(square(5))
# print(lsquare(5))
# print(product(2,3))


numbers = [1,2,3,4,5]
newl = []

# for i in numbers:
#     newl.append(lambda i : i**2)
# print(list(newl))

#map function
squareNumbers = map(lambda x : x**x,numbers)
# print(tuple(squareNumbers))
#we need to create a map function again to see the results in different data type otherwise we got an empty set of that datatype
'''print(list(squareNumbers))
print(set(squareNumbers))
print(dict(squareNumbers))'''


age  = [23,34,54,75,12]
# print(age)
newAge = list(filter(lambda x : x % 2 == 0 ,age))
# print(newAge)



#reduce
numbers = [1, 2, 3, 4, 5]
#1+2+3+4+5 >> 3+3+4+5  >> 6+4+5 >> 10+5 >> 15
sum =reduce(lambda x,y : x+y, numbers)
print(sum)


