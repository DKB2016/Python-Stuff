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


quote = """lorem ipsum dolor sit amet, consectetur adip"""
list =  []
for char in quote.upper():
    if char.isupper():
        list.append(char)
    elif char.islower():
        list.append(char)
    else:
        None
print(list)



dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
for key, value in dict.items():
    print(f"The key is : {key}, value is : {value}")
    
    

# python for loops work differently than other languages, you don't specify a starting and ending value
# you can do something similar to this with the range() function
for i in range(1, 20):
    print(f"i is {i}")
    print("i is {}".format(i))

s = "hello"
# accessing a string by positive index starting from 0
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
# accessing a string by negative index starting from -1
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
# another way of calculating the negative index is by subtracting the length of the string
print(s[0 - len(s)], 0-len(s))
print(s[1 - len(s)], 1 - len(s))
print(s[2 - len(s)], 2 - len(s))
print(s[3 - len(s)], 3 - len(s))
print(s[4 - len(s)], 4 - len(s))


nums = [ 3, 5, 4, 2, 1, 0, 9, 10, 8, 7]
print(sorted(nums)) # the sorted() method temporarily sorts the list in ascending order by default
# the sort() method permanately sorts the list in ascending order by default
# you can sort the list in descending order using the reverse() method or sort() method with the reverse parameter set to True
print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)

dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4
}

s = "onetwothreefour"
for k,v in dict.items():
    if s.endswith(k):
        dig = str(v)
    elif s.startswith(k):
        dig = str(v)
    
print(dig)

#list comprehension in python allows you to create a list of numbers from a for loop in a single line
num = [num**2 for num in range(1, 11)]
print(num)


# tuples are defined with parentheses and can be acccessed with the index notation like with lists
menu = ("Pizza", "Burger", "Salad", "Sandwich", "Chicken")

for item in menu:
    print(item)

# this fails as tuples are immutable
#menu[0] = "Chicken Burger"

menu = ("Pizza", "Burger", "Bread", "Sandwich", "Pasta")
print(menu)
print("")

for item in menu:
    print(item)
    
print("")
cars = ['audi', 'bmw', 'subaru', 'toyota', 'honda']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())