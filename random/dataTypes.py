

# strings are represented with ""
IamAString = "This is an example of a string of text"
# strings are immutable data structures

# Numeric Types are ints, floats, and complex
x = 15 # this is an int
y = 1.0 # this is a float

# Sequence types are list, tuple, and range
list1 = [1,2,3,4] # lists are ordered and mutable data structures

tuple1 = (1,2,3,4) # tuples are immutable data structured

# Mapping types are the dictionaries



my_routes = ['10.0.0.0/30','192.168.10.0/24','172.16.0.0/16']
print(my_routes)
print(type(my_routes))

print(my_routes[0])
print(my_routes[1])
print(my_routes[2])

my_routes.append("8.8.8.8/32")
print(my_routes)


# dictionarys are mutable data types and the format is in key/value pairs. 
# you access items in the dictionary with the key in square brackets
my_credentials = {
    "hostname": "192.168.31.101",
    "port": "22",
    "username": "John",
    "password": "cisco"
}

print(my_credentials["hostname"])
my_credentials["platform"] = "cisco_ios"
print(my_credentials)

commands = "router ospf 1\n router-id 1.1.1.1\n network 192.168.1.0 0.0.0.255 area 0\n"
print(commands)

# quotes within a string
banner = "this device belongs to 'theCSgroup' do not alter unless you are permitted"
print(banner)

#multiline string with three quotation marks"""
test_var = """This is a 
multi-line comment
and can spand several lines"""
print(test_var)


string = "3"
print(string)
print(type(string))

print(type(int(string)))