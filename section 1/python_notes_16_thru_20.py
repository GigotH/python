
"""
list
"""

friends = ["Eli", "Armin", "Cam"]

print(friends[0])
print(len(friends))

friends.append("John")
print(friends[3])
print(friends)

friends.remove("John")

friends_ages = [["Eli", 61], ["Armin", 22], ["Cam", 57]]
print (friends_ages[0][1])

"""
Better to split list of list into multiple lines, like:

friends_ages = [
    ["Eli", 61], 
    ["Armin", 22], 
    ["Cam", 57]
]

"""

friends_ages.append(["John", 64])
print(friends_ages)


"""
tuples

once established, a tuple cannot be appended to
"""

short_tuple = "Eli", "Armin"
a_bit_clearer = ("Eli", "Armin")  # In most cases the brackets are not required, but make it clearer when 
# viewing the code that it is a tuple.  And in some cases, without the brackets, Python cannot determine if 
# the comma is a separator for a tuple, or something else.  Brackets are needed if you have a tuple inside
# a list.
tuple_in_list = [("Eli", "Armin", "Cam")]
print(tuple_in_list)

friends = ("Eli", "Armin", "Cam")
print(friends)

friends = friends + ("John",)
print(friends)



"""
sets - don't hold order and don't contain duplicate elements
"""

art_friends = {"Picasso", "Rembrandt", "Michelangelo"}
science_friends = {"Einstein", "Oppenheimer"}

art_friends.add("Armin")
science_friends.add("Michelangelo")

print(art_friends)
print(science_friends)

art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)
not_in_both = art_friends.symmetric_difference(science_friends)
art_and_science = art_friends.intersection(science_friends)
all_friends = art_friends.union(science_friends)

print(art_but_not_science)
print(science_friends)
print(not_in_both)
print(art_and_science)
print(all_friends)

nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
friend = input("Enter the name of a friend: ")

print(friend)

# Add the name to the empty set
user_friends.add(friend)

print("user_friends:")

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
all_friends = nearby_people.intersection(user_friends)
print(nearby_people)
print(all_friends)


























