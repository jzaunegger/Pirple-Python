# Functions
* Functions are sections of code that can take in arguments and calculate something for you. Functions are nice to utilize because it allows the developer to resuse that section of code without having to repeat the process of typing it all out again and again. Good examples of this are things like math calculations. Any input that you give a function is only availble inside the scope of that function, so what you call arguments does not matter as much.

## Basic Structure
* You use the def keyword to define the creation of a function, then you give the function an name, and pass in arguments into parentheses, you end the line with a colon. Python is very sensitive to whitespace, so any line after declaring a function must be indented. Then you do some sort of calculation inside of the function, and return some output using the keyword return.

## Examples
```python
def FunctionName(argument):
    # Some sort of calculation goes here
    return null

def addOne(number):
    number += 1
    return number

output = addOne(1)

# The value of output is now two!
```
