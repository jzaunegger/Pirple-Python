"""
Homework 4 for the Pirple Python-Is-Easy Course
Author: jzaunegger
Date: November 5th, 2020

About: 
    This homework is about getting hands on experience
    creating and using lists. 
"""

# Add to the Leftover List
########################################################################
def addLeftover(rejectedList, newItem):
    rejectedList.append(newItem)

# Create a function to add things to the list
########################################################################
def addListItem(inputList, rejectedList, newItem):

    itemFound = False

    # Check if the new item is in the list
    for entry in inputList:
        if(entry == newItem):
            itemFound = True
    
    # If the new item already exists, return False
    if(itemFound):
        addLeftover(rejectedList, newItem)
        return False

    # If the new item does not exist, return True
    else:
        inputList.append(newItem)
        return True

def printLists(inputList, leftoverList):
    print("-------------------------------------------------")
    print("Input List:", inputList)
    print("Rejected List:", leftoverList)


# Main Program 
########################################################################

print("-------------------------------------------------")
print("Running Homework 4")
print("Author: jzaunegger")

# Create Empty Lists
myUniqueList = []
myLeftovers = []

# Add a number
val1 = addListItem(myUniqueList, myLeftovers, 1)
val2 = addListItem(myUniqueList, myLeftovers, 1)
printLists(myUniqueList, myLeftovers)

# Add some letters
val3 = addListItem(myUniqueList, myLeftovers, "a")
val4 = addListItem(myUniqueList, myLeftovers, "A")
printLists(myUniqueList, myLeftovers)