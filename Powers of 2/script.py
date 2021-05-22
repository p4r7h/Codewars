# Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n (inclusive).

def powers_of_two(n):
    asd = []
    for j in range(n+1):
        number = 2 ** j
        asd.append(number)
    return (asd)
