# dictionary uses {}

friend_ages = {"Tim": 47, "Casey": 37, "Sasa": 42, "Craig": 52}

for name in friend_ages:
    print(name)

for age in friend_ages.values():
    print(age)

for name, age in friend_ages.items():
    print(f"{name} is {age} years old.")




