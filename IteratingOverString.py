#
# Created on Fri Aug 05 2022
# by David J. Clark
# scarletspeedster1729@protonmail.ch
# IteratingOverString.py
# Copyright (c) 2022
#

print("This will check to see if there are any upper case letters and display them.")
text = input("Please enter a quote: ")

for char in text:
    if char.isupper():
        print(char)


for char in text:
    if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(char)
