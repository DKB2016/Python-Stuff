#
# David Clark
# 11/27/23
#

fav_bball_team = "Boston Celtics"
fav_futbol_team = "Real Madrid"

first_name = "david clark"

lowercase_name = "harry"

#
# Standard built-in methods for python3 strings

# capitalize()
print(lowercase_name.capitalize()) # will print the first letter 
#name = input("What is your first name? ")
#print(name.capitalize())

# count(x, [y, z])
# this method will return the number of times x appears from y to z
state = "mississippi"
print(state.count("i")) # this will return 4
# you can optionally start from a specific index and stop at a specific index
print(state.count("i", 1, 5)) # this will return 2
count = state.count("i", 1, 5)
print(type(count))