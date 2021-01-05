ages = [37, 42, 47, 52, 57]

odds = [age for age in ages if age % 2 == 1]

print(odds)


friends = ["Tim", "Sasa", "casey", "Craig", "gigot"]
guests = ["Casey", "brad", "Craig", "andrew" "cole"]

# turn them in to sets so we can do intersection
friends_lower = set([f.title() for f in friends])
guests_lower = set([g.title() for g in guests])

print(friends_lower.intersection(guests_lower))

#  or....don't use sets

present_friends = [
    name.title() 
    for name in guests 
    if name.title() in friends_lower
]

print(present_friends)

