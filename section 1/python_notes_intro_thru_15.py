#  variables can only contain letters, underscores or numbers and should be lower case, such as variable_name.  variable names cannot begin with a number
#
# if a variable's value will never change, it is considered a constant, and should be all upper case.
# 

#  Lists vs. Tuples vs. Sets

#  grades = [80, 75, 90, 100]  <== (List) un-ordered, can contain duplicates, values can be added / removed modified.
#  grades = (80, 75, 90, 100)  <== (Tuple)  ordered, can contain duplicates, values can NOT be added / removed modified.
#  grades = {80, 75, 90, 100}  <== (Set) un-ordered, can NOT contain duplicates, values can be added / removed modified, good for when you need to compare or combine collections of values between sets.


#########  numbers:  integers & float (floating point)
#  division with a single "/" will always return a float.  If you want an integer returned, use "//" (does not round up/down)


age = 57
print(age)

age_in_months = age * 12
print(age_in_months)

maths_operation = 1 + 3 * 4 / 2 - 2
print(maths_operation)

maths_operation = 1 + 3 * 4 // 2 - 2
print(maths_operation)


integer_div = 13 // 5
print(integer_div)

# modulus "%" returns the remainder.  
remainder = 13 % 5
print(remainder)

# divide anything by 2 using modulus and it will always be 0 for even numbers and 1 for odd numbers
oddnum = 99
evennum = 88
remainder = oddnum % 2
print("remainder: ", remainder)
remainder = evennum % 2
print("remainder: ", remainder)

#######  text

my_string = ' I want to say "Hello, world!"'
print(my_string)

multiline = """Hello, world.

some more lines
some more lines

wow, that was long"""

print(multiline)

#  This can also be used for comments instead of #.  This would be a comment:

"""
These are effectively comments....
This program does x
this program does y
this program does z
"""

name = "Jose"
greeting = "Hello, " + name
print(greeting)

age = 57
age_as_string = str(age)

print("You are " + age_as_string)

"""  
f-strings (format strings) - does the conversion on the fly.  can be used with strings and numbers.
"""

print(f"You are {age}")

greeting = f"How are upi {name}?"
print(greeting)

final_greeting = "How are you, {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)

final_greeting = "How are you, {name}?"  # note, not an f-string
jose_greeting = final_greeting.format(name="Jose")  # could also be jose_greeting = final_greeting.format(name=name)  since we also have a variable named "name"
print(jose_greeting)


"""
Getting user input
"""

my_name = "Gigot"
#your_name = input("enter your name: ")  # prompts for user input value is always a string
#age = input("Enter your age: ")
#age_num = int(age)
"""
The above two lines could be replaced with a single line that gets the user input and converts into an int:

age_num = int(input("Enter your age: "))
"""
#months = age_num * 12

#print(f"Hello {your_name}, My name is {my_name}")
#print(f"You have lived for {months} months.")

"""
booleans

True or False (proper case)
"""

#age = int(input("How old are you: "))
#is_over_age = age >= 18
#is_under_age = age < 18
#is_twenty = age == 20

#print(is_over_age, is_under_age, is_twenty)

my_number = 8
#user_number = int(input("Can you guess my number?  Enter your guess: "))

#print("My number: ", my_number)
#print("Your guess: ", user_number)

#matches = my_number == user_number

#print(f"You got it right: {matches}")

"""
and & or
"""

age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150
print(f"You can learn programming: {can_learn_programming}.")

usually_working = age >= 18 and age <= 65
print(f"At age {age}, you are usually working: {usually_working}.")


print(bool(20))  #  boolean of non-zero or non-null values are always True
print(bool("something"))

print(bool(0))  #  boolean of zero or null values are always False
print(bool(""))

# "and"
x = 35 and 2  # evaluates the first entry (35), which returns "True", so it returns the second value (2)
print(x)

x = 0 and 2 # evaluates the first entry (0), which returns "False", so it returns the first value (0)
print(x)

# "or"
x = 35 or 2  # evaluates the first entry (35), which returns "True", so it returns the first value (35)
print(x)

x = 0 or 2 # evaluates the first entry (0), which returns "False", so it returns the second value (2)
print(x)

name = ""
surname = "Smith"
greeting = name or f"Mr. {surname}"
print(greeting)

name = "Cam"
greeting = name or f"Mr. {surname}"
print(greeting)

# not

print(not bool(35))   # "not" returns the opposite.  So, bool of 35 returns True, so the out put is False.
print(not 35)   #  you can elimitate the "bool()", because Python knows that "not" is used with booleans
print(not 0)    #  bool of 0 is False, so the output is True

