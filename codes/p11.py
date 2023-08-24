#Sets

data =  {21,23,43,12,21}
data1  = set() # to create an empty set we have to use set function
data2 = {3,21}
# print(type(data1))

# to access set
for u in data:
    # print(u)
    pass


#set Methods


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
#union() methods print all the elements present in both sets



cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
# update() method adds item into the existing set from another set



cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
#intersection() method returns a new set of common elements



cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
#intersection_update() method updates into the existing set from another set.



cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
#The symmetric_difference() method returns a new set of unmatched items




cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
#symmetric_difference_update() method updates into the existing set from another set.




cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
#The difference() method returns a new set of those only items that are only present in the original set and not in both the sets.



cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi","Berlin"}
# difference_update() method updates into the existing set from another set.



set1 = {1,2,3}
set2 = {4,5,6}


print(set1.isdisjoint(set2)) #The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

print(set1.issuperset(set2)) #The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.


set1.add(4) # to add an element
# set1.clear() #clear the set elements
set4 = set1.copy() #generate a copy of set
a = set1.pop() #remove the last item of set and store the deleted value in a variable
set1.remove(3)#remove specific item

# print(set1)
