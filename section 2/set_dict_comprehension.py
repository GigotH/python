friends = ["Tim", "Sasa", "casey", "Craig", "gigot"]
guests = ["Casey", "brad", "Craig", "andrew" "cole"]

# turn them in to sets so we can do intersection
friends_lower = {f.lower() for f in friends}
guests_lower = {g.lower() for g in guests}

present_friends = {name.title() for name in friends_lower.intersection(guests_lower)}


print(present_friends)

time_since_seen = [3, 7, 5, 20, 12]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
}

print(long_timers)

# create a dictionary from the two lists but only containing the ones with time_since_seen greater than 5
long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

"""
could also be written as:
long_timers = {friends[i]: time_since_seen[i] for i in range(len(friends)) if time_since_seen[i] > 5}

"""

print(long_timers)
