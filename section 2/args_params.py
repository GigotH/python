car = {
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fuel_consumed": 460
}

# begin function definition.  NOTE:  "car_to_calculate" could be "car", and it would not use the one defined above.
def calculate_mpg(car_to_calculate):
    mpg = int(car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"])
    name=f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon.")
# end function definition


calculate_mpg({
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fuel_consumed": 460
})  #  passes the parameter values to the function as an argument

calculate_mpg(car)  # passes the car variable at line 1 to the function

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235}
]

for each_car in cars:
    calculate_mpg(each_car)



# begin function definition with two arguments/parameters. 
def calculate_mpg_2(car_to_calculate, intro):
    print(intro)
    mpg = int(car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"])
    name=f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon.")
# end function definition


for car in cars:
    calculate_mpg_2(car, "This is a car")  #  In this case we're passing the 2nd parameter as static text, but in the real world it would probably be another variable

