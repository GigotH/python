cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235}
]

def calculate_mpg(car):
    mpg = int(car["mileage"] / car["fuel_consumed"])
    return mpg  # as soon as a function encounters a return statement, it ends, even if there is more code below the return within the function block.


def car_name(car):
    name=f"{car['make']} {car['model']}"
    return name


# example of function that takes two arguments
def print_car_info(car_name, car_mpg):
    print(f"{car_name} does {car_mpg} miles per gallon.")


for car in cars:  # use values returned from two functions and pass both to another function to print.
    mpg = calculate_mpg(car)
    name = car_name(car)
    print_car_info(name, mpg) 
    
############
print()
print()
############

#  another way  would be to have the print function call the other two functions

def print_car_info2(car):
    name = car_name(car)
    mpg = calculate_mpg(car)
    print(f"{name} does {mpg} miles per gallon.")  # Note, we're printing it as part of the function.  Alternatively we could return the string
                                                   # and instead of just calling it below, we would print the return value:
                                                   #    print(print_car_info2(car))


for car in cars:
    print_car_info2(car)


#  you can have multiple returns in a function if they are within an if statement, so only one would ever get executed.
def divide(x, y):
    if y == 0:
        return "You tried to divide by zero!"
    else:
        return x / y


print(divide(10, 3))

print(divide(100, 0))
