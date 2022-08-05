#
# Created on Fri Aug 05 2022
# by David J. Clark
# scarletspeedster1729@protonmail.ch
# ListsTuplesSets.py
# Copyright (c) 2022
#


# this is a list, just a 'list' of values
courses = ['History', 'Math', 'Physics', 'CompSci', 'Music', 'Gym']
print(courses) # this will print the list out

# you can access specific indices in the list
print(courses[3]) # remember lists indices start at 0, so the 3rd index is the 4th value

# slice a list with : 
print(courses[0:2]) # first number is inclusive and second one is NOT
# if you don't specify a beginning index its starts at 0
print(courses[:2]) # this is the same as above courses[:2] = courses[0:2]
# if you don't specify the second number is goes to the end of the list
print(courses[0:]) # this will print all the items in the list starting from index 0
# if you don't specify the first of the second number it will print the whole list
print(courses[:]) # this is the same as the above courses[:] = courses[0:]

# ADD ITEMS TO THE LIST
# if you want to append to the end of a list you can use the append() method
courses.append('Art') # append() will always place the new item at the end of the list
print(courses)

# you can alternatively add an item to the list with the insert() method by giving an index and value
courses.insert(0, 'Stats') # this will add this item to index 0, and shift all the other items over 1. This will not effect the other items
print(courses)

# you can optionally change an index to another value, this will remove the other value and assign a new value
courses[1] = 'Geometry'
print(courses)

# REMOVING ITEMS FROM A LIST
#
averages = [ 88, 99, 92, 65, 66, 86, 89] # lets work with a list of ints now
# if you know the index value of an item then you can remove it with the del command
del averages[3] # lets delete the lowest grade, a 65, which sits at index 3(remember index starts at 0)
print(averages) # viola no more bad grade

# if you do not know what the index is you can also remove the last item from the list with the pop() method
averages.pop() # this will remove the 89 from the list
print(averages)

# if you know the value of the item you want to remove then you can just use the remove() method
averages.remove(66) # lets remove the bad grade and add some good ones
averages.append(98)
averages.append(92)
averages.append(85)
print(averages)
# the remove() method allows you to remove an item by referencing its value

# Create an empty list and use a for loop to fill it up
emptySet=[]
for i in range(11):
    emptySet.append(i)
    print(emptySet)

# TUPLES
# Tuples are immutable lists
# Tuples use parentheses instead of brackets like lists
# You can access elements in a tuple by their index like lists
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print("")
# you can loop through a tuple just like lists
for dimension in dimensions:
    print(dimension)

# foods = input("What are you five favorite foods: ")
# print(foods)

# for char in foods:
#     print(char)

# checking if the tuple is empty
tup = (-1,)
if tup: # if this is true then it executes the for loop, if false then prints the else statement
     for i in range(101):
         tup = tup + (i,)
else:
    print("This tuple is empty!")
print(tup)







# Sequence types - list, tuple, range
# a sequence is an ordered collection of items
# anything you can iterate over is iterable
# indexing must start at 0













