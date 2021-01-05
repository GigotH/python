friends = ["Tim", "Sasa", "casey", "Craig", "gigot"]

"""
#  without enumerator

counter = 0

for friend in friends:
    print(counter)
    print(friend)
    counter = counter + 1

"""

# using enumerator:

for counter, friend in enumerate(friends):
    print(counter)
    print(friends)

print(list(enumerate(friends)))
#...is the same as:
print(list(zip([0, 1, 2, 3, 4],friends)))

# can convert to dict where the number is the key entry in the dict, and the name is that key's value
print(dict(enumerate(friends)))


# by default, enumerator starts with a value of 0, but you can change it

for counter, friend in enumerate(friends, start=3):
    print(counter)
    print(friends)

print(list(enumerate(friends, start=100)))

