#Program Name: 608-ch07-part1.py
#Assignment Module 4
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210609
#Taken from the example:
# fig06_02.py

#Import pandas

import pandas as pd

grades = pd.Series([87,100,94])

print("The value of grades[0] is",grades[0])

print("Count of Grades:\n",grades.count(),"\n")
print("Mean of Grades:\n",grades.mean(),"\n")
print("Lowest Grade:\n",grades.min(),"\n")
print("Highest Grade:\n",grades.max(),"\n")
print("Standard Deviation of Grades:\n",grades.std(),"\n")
pd.set_option('precision', 2) 

print("Describe Grades:\n",grades.describe(),'\n')


grades = pd.Series([87,100,94], index =['Wally','Eva','Sam'])

print("Eva's grades using grades['Eva']",grades['Eva'],'\n')

print("Wally's grades using grades.Wally",grades.Wally,'\n')

