friends = ["Tim", "Sasa", "Casey", "Craig", "Gigot"]

print(friends[2:4])  # prints friends[2] and friends[3], but not [4]

print(friends[1:])  #  prints from friends[1] to the end of the list (all but friends[0]).
print(friends[:4])  #  prints from the start of the list and prints friends[0] thru friends[3], but not friends[4]


print(friends[0][1:])
print(friends[4][1:4])  #  prints the [1] through [3] (but not [4]) characters of friends[4]

print(friends[-3:])  # starts at the end of the list and prints the last 3 entries.
print(friends[-3:-1])  # starts at the end of the list and prints from the 3rd from the last entry up to, but not including, the last from the list.
print(friends[:-2])  # starts at the beginning of the list and prints all but the last 2 entries.

print(friends[-4:3])  # starts at the end of the list and prints from the 4th from the last entry and the next 2 (not 3) entries.

print(friends)
