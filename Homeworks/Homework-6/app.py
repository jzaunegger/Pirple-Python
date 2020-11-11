"""
Homework 6 for the Pirple Python-Is-Easy Course
Author: jzaunegger
Date: November 11th, 2020

About: 
    Draw a gameboard with size (rows, columns) and return True.
"""

# Draw a gameboard based of off the number of rows and columns
def drawBoard(rows, cols):

    # Check if the number of rows is too big
    if(rows > 20):
        return False

    # Check if the number of cols is too big
    if(cols > 60):
        return False


    # Draw the gameboard
    for row in range(rows):
        if row % 2 == 0:
            
            for col in range(1, cols):
                if col % 2 == 1:
                    
                    if col != cols-1:
                        print(" ", end="")
                    
                    else:
                        print(" ")
                else:
                    print("|", end="")
        else:
            print("-" * cols)

    # Return when complete
    return True

# Call the function with the size
drawBoard(20, 50)
            