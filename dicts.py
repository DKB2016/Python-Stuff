my_dict = {"name": "David", "age": 28, "city": "Decatur"}
print(my_dict)


try:
    print(my_dict["name"])
except:
    print("Error, not a valid key")
    
# loop over the keys in the dictionary   
for key in my_dict:
    print(key)
print('\n')
# loop over the values in the dictionary
for value in my_dict.values():
    print(value)