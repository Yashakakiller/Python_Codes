#input (returns a value) >> accept string as default

# name = input("Enter your name : ")
# print("My name is",name)

#n1 = int(input("Enter number 1 : "))
#n2 = int(input("Enter number 2 : "))
# print(n1 + n2)

# print(n1 + n2 , n1 - n2 , n1 * n2 , n1/n2 , n1 // n2 , n1 ** n2 , n1 % n2)



# Strings >> immutable
#EOL = End Of Line
name = "Yash"
friend = 'Krishna'
debate = '''
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[34]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[35][36]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[37] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.
'''

# print(debate)

#print(name[0]) >>> Y
#print(name[4]) >>> Index out of range


# for ch in debate:
#     print(ch)


name = "Mahadev Loves+Me"
# print(name[:7])
# print(len(name))

#print(name[:]) >> here it puts length at the end 
#print(name[0:-2]) >> till the third last character

# print(name[-1:-3])


# Strings Methods
name = "                !!yash!!yash! Mahadev"
print(name.strip())
print(name.upper())#all upper
print(name.lower())#all lower
print(name.capitalize())#first letter upper
print(name.rstrip("!"))#remove ! from last
print(name.lstrip("!"))#remove ! from start
print(name.replace("yash","mahadev"))#remove yash with mahadev
print(name.split(" "))# it returns an array with the elements having " " between them in string
print(name.center(90))#changes the position 
print(name.count("!"))#count the occurance of a particular 
print(name.endswith(""))#checks wether the string ends with particular or not
print(name.endswith("yash",7,12,))#check at the specifjc position
print(name.find("krishna"))#return the index of first occurance and return -1 if not
#print(name.index("yashu"))#if want an error then use index () otherwise find()
print(name.isalnum())#return true if 0-9 A-Z a-z if present only >> aplha numeric
print(name.isalpha())#return true if a-z or A-Z
print(name.islower())# check the string is lower
print(name.isprintable())#return true if include valid characters 
print(name.isspace())# return true only when it includes space
print(name.title())# capitailize each letter of every word
print(name.swapcase())#changes the upper into lower or lower into upper
print(name.startswith("!!"))#checks the starting word
'''n = "intro for python"
q = n.split(" ")
for x in q:
    print(x)
    print(x.capitalize(),"\n")'''