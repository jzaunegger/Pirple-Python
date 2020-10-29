"""
Homework 2 for the Pirple Python-Is-Easy Course
Author: jzaunegger
Date: October 29th, 2020

About: 
    This homework is about getting hands on experience
    creating and using functions that return data.
"""

# Function that returns the Musical Genre
def genre():
    return ["Hip Hop", "Rap"]

# Function that returns the Artist Name
def artist():
    return "Wiz Khalifa"

# Function that returns the Year Released
def year():
    return 2012

# Function that takes in a value and checks if it matches "Wiz Khalifa"
def checkArtist(value):
    if(value == "Wiz Khalifa"):
        return True
    else: 
        return False


# Print the value returned from each function
print(genre())
print(artist())
print(year())
print(checkArtist("Wiz Khalifa"))