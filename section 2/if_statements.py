friend = "Eli"

user_name = input("Enter your name: ")

#  Colon required at the end of the boolean
if user_name == friend:
    print(f"Hello, {friend}")
else:
    print("Hello, stranger!")

print(bool(5))  # resolves to True

if 5:  # always resolves to True
    print("do something")  # will always print since boolean of 5 is always True

name = input("Enter your name: ")

if name:
    print(f"Your name is {name}")
else:
    print("You did not enter anything.")

friends = ["John", "Jim", "Sasa"]
family = ["Eli", "Armin", "Mel"]

user_name = input("Enter your name: ")


# "in" keyword checks to see if something is in a collection

if user_name in friends:
    print("Hello, friend!")
elif user_name in family:
    print("Hello, family!")
else:
    print("I don't know you")
