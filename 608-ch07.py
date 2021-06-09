#Program Name: 608-ch07.py
#Assignment Module 4
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210608
#Taken from the example:
# fig06_02.py

#Import pandas

import pandas as pd

grades_dict = {'Wally':[87,96,70], 'Eva':[100,87,90],'Sam':[94,77,90],'Katie':[100,81,82],'Bob':[83,65,85]}

grades = pd.DataFrame(grades_dict)
grades.index =  ['Test1','Test2','Test3']

print(grades)

#print(grades[0])
print("This is grades at in index of 0:\n",grades.iloc[0],"\n")
print("Count of Grades:\n",grades.count(),"\n")
print("Mean of Grades:\n",grades.mean(),"\n")
print("Lowest Grade:\n",grades.min(),"\n")
print("Highest Grade:\n",grades.max(),"\n")
print("Standard Deviation of Grades:\n",grades.std(),"\n")
pd.set_option('precision', 2) 

print("Describe Grades:\n",grades.describe(),'\n')

print("Eva's grades\n",grades['Eva'],'\n')

print("Wally's grades\n",grades.Wally,'\n')

print("A series values of Test1\n",grades.loc['Test1'])

