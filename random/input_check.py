
# show command = "show ip int bri"

show_command = input("Enter the show command you wish to execute ")
print(show_command)

name = input("What is your name? ")
age = input("What is your age? ")

message1 = "Hello {fname}, your are {fage} years old".format(fname=name, fage=age)
print(message1)

message2 = "Hello {0}, you are {1} years old today!".format(name, age)
print(message2)