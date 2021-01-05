"""
dictionairies  (keys/values)
"""

friend_ages = {"Eli": 61, "Gigot": 57, "Armin": 22}

print(friend_ages["Eli"])

friend_ages["Oma"] = 98

print(friend_ages["Oma"])

print(friend_ages)


"""
tuple containing a dictionary
"""

friends = (
    {"name": "Eli Hudspth", "age": 61},
    {"name": "Gigot Hudspeth", "age": 57},
    {"name": "Armin Hudspeth", "age": 22}
)

print(friends[0]["name"])

# A dictionary key's value can be assigned to a variable, then the variable used instead of the key's index number:
friend = friends[2]
print(friend["name"])


print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

# dict function
# list of tuples:
friends = [("Eli", 61), ("Gigot", 57), ("Armin", 22)]

# turn it into a dictionary using the "dict" function:

friend_ages2 = dict(friends)

print(friend_ages2)



