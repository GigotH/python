for n in range(2, 100):
    for x in range(2,n):  #  all numbers between 2 and current 'n', excluding current 'n' (2 thru n-1)
        if n % x == 0:  #if n divided by one of the numbers between 2 and n-1 does not have a remainder, it is divisible by two numbers other than 1 and itself, and not prime.
            print(f"{n} equals {x} * {n//x}")
            break
    else:  # this executes if the 2nd "for" loop completed without ever executing the "break".  So it never found a combination of numbers between 2 & n-1 that n could be divided by without a remainder.  So it is prime
        print(f"{n} is a prime number.")