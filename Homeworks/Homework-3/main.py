"""
Homework 3 for the Pirple Python-Is-Easy Course
Author: jzaunegger
Date: November 1st, 2020

About: 
    This homework is about getting hands on experience
    creating and using if statments and conditional logic.
"""

def compare(arg1, arg2, arg3):

    # Check if arguments are strings, 
    # if so convert them to int
    if(type(arg1) == str):
        arg1 = int(arg1)

    if(type(arg2) == str):
        arg2 = int(arg2)

    if(type(arg3) == str):
        arg3 = int(arg3)


    # Compare if Arguments are Equal
    if(arg1 == arg2):
        return True
    
    if(arg2 == arg3):
        return True
    
    if(arg1 == arg3):
        return True

    else: 
        return False


print(compare(1, 3, "3"))