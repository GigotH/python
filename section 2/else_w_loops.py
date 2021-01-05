# can be used with for loops and while loops

# cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]
cars = ["ok", "ok", "ok", "ok", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}.")
    print("shipping new car to customer")
else:
    print("All cars built successfully. no faulty cars!")  # 'else' in a for loop only gets executed if the 'break' was never executed, and no errors were encountered.


