#list  >> ordered collection
list1 = [1,2,3,4,5,6,7,8,9,0]
# print(type(list1) ,list1)

#print(list1[len(list1)-3])#negative into positive indexing


#using in operator
if( 52 in list1):
    # print("yes")
    pass
else:
    # print("no")
    pass

#print(list1[1:-1:2])#-1 => len(list1) - 1 => 5 -1 = 4



#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ["hello".upper() for a in fruits if len(a) > 4]

# print(newlist)


#list methods
data = [11,2,31,2,3,4,5]
# data.append(6)
# data.sort()
# data.sort(reverse=True)
# data.reverse() #it simply reverse the list elements not in the context of sorting
# print(data.index(2)) #index of first occurence
# print(data.count(2))

#this will change the data list too
tryData = data #data list pass its address reference
tryData[0] = 0


#to make a copy of list without changing the other list
copyData = data.copy()
copyData[0] = 1212
# print(tryData , data) # same thing will print
# print(copyData)


# data.insert(1, int("899"))
# data.extend(copyData)
# data.pop(2)  #[0, 2, 31, 2, 3, 4, 5]
# data.clear()
# data.remove(2) #remove first occurenece of 2


# print(data)







#tuples
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)





#enumerate function

print("\n\n")
marks = [1,2,4,5]
'''index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("highest score")
    index+=1'''

for index,mark in enumerate("apple",start=1):
    print(index,mark)
    if(index == 3):
        print("highest score")
    