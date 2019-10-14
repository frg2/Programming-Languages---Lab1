#Lab 1

#Importing necessary functions
import math

#Task 1

course = "python "
rating = 5

print(course + str(rating))

#Task 2
b = 3
c = 4

#Using the math square-root function
a = math.sqrt((b**2) + (c**2))
print(a)

#Task 3
#printing the data type of the variables
print(type(a))
print(type(b))
print(type(c))

#Task 4
#Changing the data type of a
a=int(a)
print(type(a))

#Concatination
print(str(a) + " squared equals " + str(b) + " squared " + str(c) + " squared.")

#Task 5
#largest function finds the largest item in the list
def largest(intlist):
  maxvalue = intlist[0]
  for item in intlist:
    if (item > maxvalue):
      maxvalue = item
  return maxvalue

#Test Lists  
print (largest([1,2,3,4,5,6,7,8,9,0]))
print (largest([1,2,3,4,5,6,7,8,9,0]))
print (largest([5,4,3,3,2,1]))
print (largest([1,2,3,4,5,6,7,8,9,10]))
print (largest([1,1,1,1,1,1,1]))
print (largest([1.0,2.0,3.0,4.0,5.0,6.0]))
print (largest(['a','s','d','f','g','h','i','j','k','l']))


#Task 6
#Creates the title and first line of the multiplication square
def timestables():
  print("Here is a number square:")
  print("\t", end = '')
  for x in range(1,10):
    print(str(x) + "\t", end = '')
  print()

#This function prints each line, if it is the first item then it'll just print the multiplier
def multiple(multi):
 for x in range(0,multi+1):
   if(x == 0):
     print(str(multi) + "\t", end = "")
   else:
    print(str(multi*x) + "\t", end = '')
 print()

timestables()
for i in range(1,10):
  multiple(i)
