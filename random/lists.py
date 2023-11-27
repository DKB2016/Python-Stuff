
#
#
#

alabama_roster = ["Tyler Buchner", "Ty Simpson", "Jalen Milroe", "Jase McClellan", "Justin Jefferson", "Kool-Aid McKinstry", "Jermaine Burton"]

for _ in alabama_roster:
    print(_)

# appending to a list allows you to add to the end of a list
alabama_roster.append("Nick Saben")
print(alabama_roster)

# you can insert at any position(index) by using the insert() method
print(alabama_roster)
alabama_roster.insert(2, "Bryce Young")
print(alabama_roster)