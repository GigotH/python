friends = ["Tim", "Casey", "Sasa", "Craig"]

# for friend in friends:
#     print(friend)

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for _ in elements:  # Python best practice is to name the for loop's variable "_" if you're not going to use the actual variable in the loop
#     print("Hello, world!")

"""
range
"""

# for _ in range(10):  # This has the same result as the above
#     print("Hello, world!")

# for index in range(5, 10):  # This prints the range from 5 to 10, not including 10.  (5 6 7 8 9)
#     print(index)

# for index in range(2, 20, 3):  # This prints the range from 2 to 20 not including 20, but only every 3rd number.  (2 5 8 11 14 17)
#     print(index)

students = [
    {"name": "Eli", "grade": 100},
    {"name": "Armin", "grade": 95},
    {"name": "Gigot", "grade": 88},
    {"name": "Phil", "grade": 80}
]

for student in students:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has a grade of {grade}.")

    

