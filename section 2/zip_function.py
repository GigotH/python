#  zip combines two lists where each element of the new list is a tuple of elements.

friends = ["Tim", "Sasa", "casey", "Craig", "gigot"]
time_since_seen = [3, 7, 5, 20, 12]

new_list = dict(zip(friends, time_since_seen))
print(new_list)


"""
long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
}

print(long_timers)
"""

