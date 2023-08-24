#loops

name = 'yash'
data = ["yash","akshat","rachit","tanishk","harsh"]
for i in data:
    for j in i:
        # print(j,end=",")
        pass  # used to pass empty body in block
# print("\n")
for i in name:
    if(i == "s"):
        # print("something is special")
        pass
    else:
        # print(i,end=",")
        pass


for k in range(0,5,2):
    # print(k,end=" ")
    pass

'''num = int(input("enter number : "))
for i in range(0,11):
    print(i,"*",num,"=",i*num)'''


#while loops
i = 5
while( i > 0):
    # print(i)
    i-=1
else:
    pass
    # print("sorry i am not greater than 0")

#how we can implement do - while loop
'''while True:
    number = int(input("enter"))
    print(number)
    if not number > 0:
        break'''


for i in range(1,11):
    if(i == 3):
        continue #skip the iteration
    print(i)

print("\n")
for i in range(1,11):
    if(i == 3):
        break #break the loop
    print(i)



#ELSE WITH LOOPS
print("\n\n")

for i in range(5):
    print(i)
else:
    print("hello")