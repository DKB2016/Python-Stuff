# messin' with whitespace and strings


name = "David  "

print(name)
print(len(name))


# .strip() method takes white space 
Sname = name.strip()
print((Sname))
print(len(Sname))


#lists
# Lists allow you to store sets of information in one place, whether you have a few items or millions of items
# Lists are a collection of items in a particular order - order matters, but can have duplicates
grocery_list = ['apples', 'cereal', 'bananas', 'milk', 'bread', 'chicken']
# this is how a list is defined. 
#you can access items in your list with indices, starting at 0. 
print(grocery_list[0]) # this will print out 'apples'
first_item_in_list = grocery_list[0]
print(first_item_in_list) # this is the same as the print with index 0. 
# another example
names = ['chris', 'clay', 'tammy', 'atom', 'john', 'tom', 'jimmy', 'james', 'bartholemu']
# what if I want to make sure names are capitalized appropriatly ?
print(names[0].title()) # this will give 'David' even though in the list it shows as 'david'
print(names[1].title()) # this will give 'Clark' even though in the list it shows as 'clark'
# .title() is a method you can use on strings to capitalize first letter of each word. 
ip_address = '203.0.113.68/24' # when you count from the right it starts at -1 and goes to -length
print(ip_address[-1]) # this will return the last item in the string
# string slicing
print(ip_address[0:12], ip_address[:12]) # these are the same, 0 is implied if its not listed on the left.
print(ip_address[:3]) # this says [start:end] and in this example prints to the third(not inclusive, so second really) element.

#defining custom functions
def square_plus(x):
    return x ** 2 + 1


# f-strings or formatted strings
print(f'2^2+1 is {square_plus(2)}')
print(f'3^2+1 is {square_plus(3)}')

print(f'The first name in the list is {names[0].title()}') # this allows you to reference something in your list without having to use concatenation


# appending items to your lists
first_ten_ints = [value for value in range(11)] # range starts at 0 and is not inclusive in end argument. range(0,11) starts at 0 and ends at 10. 
print(first_ten_ints)

list1 = []
for name in names:
    list1.append(name)
    
print(list1)

# how to delete items of a list ? 
# how to delete the even numbers from your first_ten_ints list?
for int in first_ten_ints:
    if int % 2 == 0:
        first_ten_ints.remove(int)
        
#how about odd numbers ?
for int in first_ten_ints:
    if int % 2 != 0: # this only works if the numbers match their index, otherwise some items get left in the list.
        first_ten_ints.remove(int)
        
print(first_ten_ints)

list2 = [1,2,3,4]
# what if i just need the last item of the list removed ?
last_item = list2.pop() # this will store and remove the last item of the list for later use.
print(last_item)