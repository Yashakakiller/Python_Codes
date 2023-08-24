import os
#file handling

'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''

#file = open("data.txt") # same >> file = open("data.txt",'r')
# file = open("data.txt",'rt')#rt >> read and text , both are default

#print(file)#return an object

#print(file.read())#read the whole file

#print(file.read(15))#read only 15 characters


#readline function return a single line at a time
#print(file.readline())
#print(file.readline())#print the next line



#print all lines , at a time
#for text in file:
    # print(text)
    #break


#always close the file as soon as you done with that file
#file.close()

# appending in a file
#file = open("data.txt","a")# a >> append
# file.write("\nYash Gupta")
#file.close()

#file = open("data.txt")
# print(file.read())
#file.close()


# override file content
#file = open("data.txt","w")
# file.write("MAA se phele koi nahi")
# file.close()
# #file = open("data.txt")
# # print(file.read())
# file.close()




#creating a new file

#file = open("info.txt","x") #return error if file exists
# file.close()
# file = open("info.txt","a")
# #file.write("hello world this is an important information")
# file.close()
# file = open("info.txt")
# #print(file.read())
# file.close()





#delete file
# os.remove("info.txt")#it deletes that file

#check wether the file exists or not
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

# try:
#    if os.path.exists("data.txt"):
#       os.remove("data.txt")
# except:
#    print("file not found")


# delete a folder
# os.rmdir("Python Codes")



# myFile = open("myFile.txt", "r")
# for i, line in enumerate(myFile.readlines()):
#     print(i, line) # line number and content
# myFile.close()




#another way to use the file
#no need to close the file in this case
# with open("myFile.txt") as file:
#     print(file.read())



# f = open("myFile.txt")
# while True:
#     line = f.readline()
#     if not line:
#         print(line ,type(line))
#         break
#     print(line)







'''with open("myFile.txt") as f:
    i=0
    while True:
        i+=1
        line = f.readline()
        if not line:
            print(line ,type(line))
            break
        m1 = line.split(",")[0]
        m2 = line.split(",")[1]
        m3 = line.split(",")[2]

        print(f"The marks of Student {i} in maths is {m1}")
        print(f"The marks of Student {i} in science is {m2}")
        print(f"The marks of Student {i} in sst is {m3}")
    
        print(line)
'''



''' with open("myFile1.txt","w") as file:
     lines = ["This is 1 line \n","This is line 2 \n","This is line 3"]
     file.writelines(lines)
  '''  



with open("myFile1.txt","w") as file:
    file.write("hello world ! it's a nice pleasure for me to have a meeting with you . okay bye bye all my fellow techies ")
    file.seek(10)#skip the first 10 characters
    print(file.tell())#it tells how many characters we had skip
    file.truncate(2)#this will take only 2 characters in my file
    # print(file.read(6))#read only 6 characters 