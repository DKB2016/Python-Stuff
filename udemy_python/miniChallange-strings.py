#
#
#
parrot = "we win"

for _ in parrot:
    print(_)
    
new_parrot = "Norwegian Blue"
#indexing with positive indices
print(new_parrot[3])
print(new_parrot[4])
print(new_parrot[9])
print(new_parrot[3])
print(new_parrot[6])
print(new_parrot[8])

print()
#indexing with negative indices
# you can obtain the negative indexes by subtracting the string length from the index values

print()
print(new_parrot[-11]) #[3] == [-11]
print(new_parrot[-10]) #[4] == [-10]
print(new_parrot[-5]) #[9] == [-5]
print(new_parrot[-11]) #[3] == [-11]
print(new_parrot[-8]) #[6] == [-8]
print(new_parrot[-6]) #[8] == [-6]

print()
print(new_parrot[3 - len(new_parrot)])



# string slicing
#
print(new_parrot[0:6]) # slicing is up to but not including the end value
print(new_parrot[:6]) # same as above, will start at position 0 and goes up to but not including the value at position 6
print(new_parrot[10:14]) # will produce the value Blue
