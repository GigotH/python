#  Lambda functions get inputs, do a small amount of processing and return outputs
#    can do 2 things (1 or both):
#    1:  perform an action
#    2:  return an output 
#  

"""

def divide(x, y):
    return x / y

# instead of the above defined function, the same can be done with a lambda function.  In this case the name of the function is lambda_divide  

lambda_divide = lambda x, y: x / y

#  "lambda x, y: x / y" is the lambda function  

# call it like you would any other function:

print(divide(15, 3))  #  traditional function
print(lambda_divide(15, 3))  #  lambda function

#  If you don't assign a name to a lambda function, it gets created but immediately destroyed, because you can't call it....unless you pass the variable values to it on the same line.

print((lambda x, y: x / y)(15, 3))


"""
###  real world example
"""   This traditional function:
def average(sequence):
    return sum(sequence) / len(sequence)

...could be replaced by the following lambda function:
"""
average = lambda sequence: sum(sequence) / len(sequence)
# ...but it doesn't save much coding, and it is a little less "readable", so is it really appropriate for lambda function?   

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))

###   maybe BETTER real world example in "first class functions" examples.




