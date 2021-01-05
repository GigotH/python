#  create a new list succinctly


#  create a new list that is the numbers in the original list multiplied by 2
numbers = [0, 1, 2, 3, 4]



# one way...
"""
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)

print(doubled_numbers)
"""

# better way, using list comprehension...
doubled_numbers = [number * 2 for number in numbers]

print(doubled_numbers)



# some other examples

#  this does the same as above

doubled_numbers2 = [number * 2 for number in range(5)] 

print(doubled_numbers2)

friend_ages = [37, 42, 47, 52, 57]
age_strings = [f"My friend is {age} years old." for age in friend_ages]

print(age_strings)

names = ["Tim", "Casey", "Sasa", "Craig"]

lower_names = [name.lower() for name in names]  # "title" casing is first letter upper and the rest lower.  name.title() would bring back "Tim", etc, even if the value was actually "tim"

print(lower_names)



