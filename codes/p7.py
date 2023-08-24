# functions

# num1 = 8
# num2 = 3

# gmean = (num1 * num2) / (num1 + num2)

# print(gmean)


def gMeanCalculator(num1, num2):
    result = (num1 * num2) / (num1 + num2)
    if (num1 > num2):
        print("num1 is greater", num1)
    else:
        print("num2 is greater", num2)
    return result


result1 = gMeanCalculator(20, 30)


# print(result1)


def average(n1=5, n2=10):  # these are the default values
    print("The avergae is", (n1 + n2) / 2)


average(2, 8)  # it will take 2 and 8 as values in this case
average()  # it will take default value in this case

# keyword arguments
average(n2=30, n1=1)  # change the order of arguments


# this will raise error because 1 argument is missing
# def testt(a,b):
#     print(a+b)

# testt(1)


# variable length arguments
def sumNumbers(*numbers):  # by default, it takes *numbers as a tuple
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i;
        # print(i)
    print("Sum  is", sum)


sumNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("\n\n")


# recursion
def factorial(num):
    """
    this is a function which calculates factorial of a given number
    """
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))
