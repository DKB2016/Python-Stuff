#
# Created on Fri Aug 05 2022
# by David J. Clark
# scarletspeedster1729@protonmail.ch
# IteratingOverString.py
# Copyright (c) 2022
#

# print("This will check to see if there are any upper case letters and display them.")
# text = input("Please enter a quote: ")

# chars=[]
# for char in text:
#     if char.isupper():
#         chars.append(char)
# print(chars)

# for char in text:
#     if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#         print(char)

# Creates an empty list and adds all the squares from 2-100 squared to the list.
squares=[]
for num in range(2,100,2):
    squares.append(num**2)
# more concise way to do this is list comprehension
squares2=[value**2 for value in range(2,100,2)]

print(squares)
print(squares2)

# Check if they are the same
if squares == squares2:
    print("TRUE")
    
# To copy a list just use slicing with no numbers
squares_copy = squares[:]
print(squares_copy == squares)