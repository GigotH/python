def add(x, y):
    total = x + y
    return total

print(add(5, 10))


def add(x, y=3):  #  this means y is 3 by default.  It is called a DEFAULT PARAMETER  If a 2nd value is passed to the function, that value is used.  If  no
                  #  2nd value is passed to the function, 3 is used.
    total = x + y
    return total


print(add(5, 10))  #  in this case, 10 would be the value for y
print(add(5))      #  in this case, the default value of 3 would be used for y

#  when you specify the parameter values in the function call's arguments, they are called NAMED ARGUMENTS (aka KEYWORD ARGUMENT)
print(add(x=4))    #  in this case, x would 4 and y would be 3 (default)
print(add(x=5, y=6))  #  This works (two NAMED ARGUMENTS)
print(add(x=5))  #  also does, but uses the default y=3
print(add(5, y=6))  #  This works because the unnamed argument is before the named argument.
#  print(add(x=5, 6))  #  This does not work.  You cannot use an argument without a name after a NAMED ARGUMENT

"""

Also, default parameters must be at the end of the list of parameters.

These work:

def add(x, y=3): 
def add(x, y=3, z=0): 

but these do not:

def add(x=5, y): 
def add(x=5, y, z): 
def add(w, x=5, y): 
"""

print(1, 2, 3, 4, 5)  #passing 5 arguments to the print function.  The 5 parameters are printed, by default with a space between each.  
print(1, 2, 3, 4, 5, sep=" - ")  # you can specify a different separator
print(1, 2, 3, 4, 5, sep=", ")  # you can specify a different separator







