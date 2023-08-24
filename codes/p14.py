import os  #importing the whole module
from os import * #same as above

#importing specific function from module
from math import sqrt 
p1 = sqrt(9)
# print(p1)

#using as keyword as alias
from matplotlib import pyplot as plt
import numpy as np

data = np.array([[10,30,43,56],[64,76,34,77]])
# plt.plot(data)
plt.show()



#refer the practice.py file for the below code
import pracitce as py
# print(py.universalTruth)
py.greet()
