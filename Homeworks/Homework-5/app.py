"""
Homework 5 for the Pirple Python-Is-Easy Course
Author: jzaunegger
Date: November 8th, 2020

About: 
    This homework is about getting hands on experience
    creating and using loops. This assingment is called
    "Fizz Buzz".
"""

def checkIfPrime(inputNum):
    isPrime = True

    if(inputNum > 1):
        for i in range(2, inputNum):
            if(num % i == 0):
                isPrime = False
            else:
                isPrime = True
    else:
        isPrime = False
    
    return isPrime

# Print the numbers 1-100
nums = []

for num in range(1, 101):
    nums.append(num)

    #isPrime = checkIfPrime(num)
    #if(isPrime == True):
    #    print("Prime")

    # Check if the num is divisible by 3 and 5
    if(num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")

    # Check if the num is divisible by 3
    if(num % 3 == 0):
        print("Fizz")

    # Check if the num is divisible by 5
    if(num % 5 == 0): 
        print("Buzz")

    if(checkIfPrime(num) == True):
        print("Prime")

    # Print the Num
    else:
        print(num)