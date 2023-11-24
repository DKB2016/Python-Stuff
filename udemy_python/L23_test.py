#
# David Clark   
# Lesson 23-24 Udemy Python Course
# 11/22/23
#

# these are assignment operators(=)
# this is also known as binding a variable to a value
a = 12
b = 3 

print(a + b )
print(a - b)
print(a * b)
print(a / b)
print(a // b) # integer division, rounded down toward minus infinity
print(a % b) # modulo operation

print()

# range(x, y) is inclusive for x and exclusive for y
for i in range(1,4): # values in range MUST be integers
    print(i)
print()
# you can also use an operation as a parameter for range
for i in range(1, a // b):
    print(i)


# operator precedence 
print(a + b / 3 - 4 * 12) # --> this is -35.0 
# the above way is a poor way of writing this problem down but you can write parenthesis down to help with operator precendence
print(a + (b/3) - (4 * 12))


