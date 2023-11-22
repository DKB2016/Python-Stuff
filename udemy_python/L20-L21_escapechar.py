#
# David Clark   
# Lesson 20-21 Udemy Python Course
# 11/21/23
#

# this lesson is about splitting strings
splitString = "this string has been\nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# in python we use the \ - backslash as an escape character
print('the pet shop owner said "No, no \'e\'s uh,... he\'s resting".')
# or you can use tripple quotes and don't have to escape anything
print("""The pet show owner said "no, no, 'e's uh,...he's resting". """)
# you can also use triple quotes to print over multiple lines
print(""" This line
      Is
      Printed
      Over 
      Multiple
      Lines""")

#you can also escape these \n that python add's by adding a single \ at the end of the line
print(""" This line \
is \
Printed \
Over \
Multiple \
Lines""")

#
# What about escaping the escape character ?
# Lesson 21

#print("C:\Users\timbuchalka\notes.txt") # without escaping the escape character(\) python will interpret this incorrectly
print("C:\\Users\\timbuchalka\\notes.txt") # this is the correct way to escape the escape character