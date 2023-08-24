#OS MODULE
import os
if(not os.path.exists("Python Codes")):
    os.mkdir("Python Codes")

for i in range(0,100):
    # os.makedirs(f"Python Codes/Tutorial{i+1}")
    # os.rename(f"Python Codes/Tutorial{i+1}",f"Python Codes/Tutorial {i+1}")
    pass


totalFolder = os.listdir("Python Codes")
for folder in totalFolder:
    #print(folder)#accessing all folder inside the Python Code Folder
    #print(os.listdir(f"Python Codes/{folder}"))#accessing each file inside each folder of Python CODE Folder

    pass


#using system function of os Module
dateCmd = 'date'
# os.system(dateCmd)

#current working directory
print(os.getcwd())

#removes empty folder inside Python Codes Folder
for i in range(0,100):
    # os.rmdir(f"Python Codes/Tutorial {i+1}")
    pass


#os.remove("data.csv") #delete the file