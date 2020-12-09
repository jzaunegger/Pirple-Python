# Input and Output 

## Input
Python has the input keyword which is used to prompt the users console to input some value for the program to use. The input keyword allows you to send a message to prompt the user, or to just search for a input value. Input values are always read in as strings by default, you will need to cast the variable type in order to change it to something else.

```python
    # A basic input 
    inputData = input("Please enter your name.")

    # Casting for an age
    inputAge = int(input("Please enter your age."))
```

## Output
The print keyword is used to log values or messages to the console.

```python
    # A basic print
    print(inputData + "'s age is", inputAge)
```


## File Interaction
Python also allows you to read in files and interact with them. You use the open keyword with the filename and other parameters to read, write, or append data to the file. This becomes incredibly helpful and useful when combined with the os module. When working files it is very important to close the file when you are done manipulating it, this keeps errors from happening or mis-reading/writing data to the file.

File Interaction methods:
r  --> Read data from a file
w  --> Write data to a file
a  --> Append data to an existing file
r+ --> Read and write to a file.

```python
    # Open the file
    fileData = open("filename", "w")

    # Write to the file
    fileData.write("Hello, testing 1, 2, 3!")

    # Close the file
    fileData.close()
```

Python also has the csv module to handle csv files specifically. There are other modules and tools that allow for file manipulation as well, but this is pythons most basic form of file interaction.