'''

'''
import os, sys

# Main Function
def main():
    filename = input("What would you like to name your notebook? ")
    if(os.path.exists(filename)):
        print(" ")
        print("Would you like to read this file, delete this file")
        print("and start over, or add to the file, or replace a")
        print("specific line. Please enter R for read, D for delete")
        print(" A to append, or I to insert a new line.")
        print(" ")
        choice = input("Your choice: ")
        print(" ")

        # Read the file
        if(choice == "R" or choice == "r"):
            current_file = open(filename, "r")
            data = current_file.readlines()
            current_file.close()

            # Print the file
            print("File:", filename)
            print("------------------------------")
            if(len(data) == 0):
                print("This file is empty!")
            else:
                for entry in data:
                    print(entry)

        # Delete the file and start over
        elif(choice == "D" or choice == "d"):
            print("Deleting notes.")
            os.remove(filename)
            
            current_file = open(filename, 'w')
            current_file.close()

        # Insert a new line
        elif(choice == "I" or choice == "i"):

            # Read original data
            current_file = open(filename, 'r')
            og_data = current_file.readlines()
            current_file.close()

            # Get inputs
            print("Please enter what line you would like to replace: ")
            line_num = int(input("Line Number: "))

            print("Please enter the new note.")
            new_line = input()

            # Check if new line is not reachable
            if(line_num < 0):
                print("Cannot add new line to a negative index.")
                sys.exit()

            # If index is larger than length or og, add new line
            elif(line_num > len(og_data)):
                print("Adding a new line to the end.")
                current_file = open(filename, "a")
                current_file.write(new_line)
                current_file.write("\n")
                current_file.close()

            # Swap lines
            else:
                og_data[line_num] = new_line + "\n"

                os.remove(filename)
            
                current_file = open(filename, 'w')
                for line in og_data:
                    current_file.write(line)
                current_file.close()
                print("Sucessfully swapped lines")

            
        # Append to the file
        elif(choice == "A" or choice == "a"):
            
            appendage_complete = False
            current_file = open(filename, "a")

            print("When you are done adding notes,")
            print("Enter the word done.")

            while(appendage_complete == False):
                print(" ")
                print("Please enter a new note: ")
                new_line = input()

                if(new_line.lower() == "done"):
                    appendage_complete = True
                    break
                else:
                    current_file.write(new_line)
                    current_file.write("\n")

            current_file.close()






    else:
        print("The given filename does not exist.")
        print("Please restart and enter a real filename.")

main()