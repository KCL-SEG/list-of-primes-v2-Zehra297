"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def checkPrime(num):
    if num < 2:
        return False
    for i in range (2, num):
        if num % i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError(f"number of primes = {number_of_primes}. This should be > 0")
    list = []
    currentNum = 0
    while (len(list) < number_of_primes):
        if checkPrime(currentNum):
            list.append(currentNum)
        currentNum += 1
    return list
