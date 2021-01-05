def greet():
    print("Hello")


greet()

# the function can be referred to as just "greet" if you are not wanting to run it, but just refer to it.  for example:

greet_value = greet

greet_value()

#####################

def average(seq):
    return sum(seq) / len(seq)


avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)  # since sum and max are built in functions, this could be done by calling them directly:  "total": sum
top = lambda seq: max(seq) # since sum and max are built in functions, this could be done by calling them directly:  "top": max



students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")

    operation = input("Enter the operation you would like to perform, 'average', 'total' or 'top': ")

    if operation.lower() == "average":
        print(avg(grades))
    elif operation.lower() == "total":
        print(total(grades))
    elif operation.lower() == "top":
        print(top(grades))
    else:
        print(f"You did not enter a valid value for {name}")


###  a better way:

operations = {
    "average": avg,
    "total": total,
    "top": top
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation_entered = input("Enter the operation you would like to perform, 'average', 'total' or 'top': ")

    operation_function = operations[operation_entered.lower()]  # this gets maps the name of the lambda function to run from the "operations" dictionary defined above, based on what the user entered.
    print(operation_function(grades))  #print the output of the operation_function (avg, total or top) lambda function, passing the values of the grades tuple for the student
    #  NOTE, the downside of this is that the above method using the if/elif/else statements would not generate an error if something other than average, total or top was entered.
    #        with this method, if something else was entered, it will generate an error.  Error handling can resolve that...once we get to error handling

"""
The lambda functions could be incorporated into the dictionary, but that makes the code sort of complicated.   May not be best practice.

operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": lambda seq: sum(seq),  # since sum and max are built in functions, this could be done by calling them directly:  "total": sum
    "top": lambda seq: max(seq)  # since sum and max are built in functions, this could be done by calling them directly:  "top": max
}



"""




