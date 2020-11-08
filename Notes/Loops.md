# Loops
Loops are used to iterate through data, and are common tools used to develop complex applications. These are one of the main components of programming. There are a variety of loops in python such as for loops, while loops, and do while loops.

## For Loops
For loops in python will automatically infer a step value based on the object being iterated. For example when iterating through a string, each step will be a single letter starting from the beginning of the word. They use the for in format. 

```python
    word = "hello"

    for letter in word:
        print(letter)

    # Output
    # h
    # e
    # l
    # l
    # o

```

Loops can also be used in other ways such as the example below. Instead of the range of the iteration being declared by a variable, it is given via a integer in the loop. Range can take three parameters (startingValue, endingValue, stepSize). The loop starts at the index of the starting value, and increments by stepSize up to but not including the endingValue.

```python

    for num in range(0, 5, 2):
        print(num)

    # Output
    # 0
    # 1
    # 2
    # 3
    # 4 
```

## While
While loops execute a certain code block while some condition has not been met. Given the example below, the counter will increment while the counter is less than 10.

```python
    counter = 0

    while(counter < 10):
        counter += 1
```

## Break and Continue
When talking about lists, two keywords pop-up when talking about loops.
* Break - Refers to the keyword to use when you want to leave a loop when some condition is met. In the first example below, the loop is broken if num is equal to 3.

```python
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for num in nums:
        if num == 3:
            break

        print(num)
```

* Continue - Continue is used when you detect some condition and do not want to execute a code block, but also want to keep iterating through the loop. So this keywork ignores the current codeblock but keeps moving through the loop.