cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}.")
    print("shipping new car to customer")


for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping it!")
        continue  # does not execute the other commands in the for loop for this iteration, jumps to the beginning of the for loop for the next item in the list
    print(f"This car is {status}.")
    print("shipping new car to customer")

