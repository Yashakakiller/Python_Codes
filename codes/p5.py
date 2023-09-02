import time

#if-else condition

#conditional operator
# > , <  ,>= , <= , ==

# age = int(input("Enter Your Age : "))
# print("Your age is",age)

'''if(age >= 18):
    print("You can drive")
    print("yes")
else:
    print("you cannot drive")
    print("no")
print("hello")'''


'''if(age > 18):
    print("yeah! you can drive")
elif(age == 18):
    print("yeah , congrats ,now you can drive")
elif(age <=10):
    print("abhi toh dudh k daat bhi nahi aaye bhai")
else:
    print("ruko jara sabar karo")'''


#nested codes
'''num = int(input("enter your number : "))
if(num < 0):
    print("number is negative")
elif(num > 0):
    if(num <= 10):
        print("number lies between 0 and 10")
    elif(num > 10 and num <=20):
        print("number lies between 10 and 20")
    else:
        print("number is greater than 20")
else:
    print("number is 0")'''


# a = 1000
# b = 1000
# print("a is greater") if a > b else print("b is greater") if( b > a) else print("both equal")



timestamp = time.strftime("%D : %H : %M : %S : %Z")
print(timestamp)
h = int(time.strftime("%H")) #by default it return in string format for that we need to do type casting
if(h >= 00 and h < 12):
    print("good morning")
elif(h>= 12 and h < 14):
    print("good afternoon")
elif(h>= 14 and h < 19):
    print("good evening")
else:
    print("good night")







#using match case statements
#no need of break keyword for developers from c or c++
num1 = 5
'''match num1:
    case 0:
        print("number is 0")
    case 5:
        print("number is 5")
    case _ if num1 != 10: #default case with condition
        print("number is not 10")
    case _ : # default case
        print("number is 10")'''


