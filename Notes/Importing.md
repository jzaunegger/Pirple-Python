# Importing

Python allows developers to build modules or packages using classes and functions that you may carry across projects, or share with others. There are a lot of pre-existing packages that you can import into your projects, that offer a wide range of functionality to python. When dealing with package management, there are two main groups of packages, internal or built-in python module like randomm, time, or math. Then there is external packages that are open-sourced or maintained by a community of developers.

```python
    # Import math and random.
    import math
    import random as r

    randInt = r.randint(1, 10)
    randSqu = math.pow(randInt, 2)

    print(randInt, randSqu)

    # >>> (1, 1)
    # >>> (2, 4)
    # >>> (3, 9)
    # >>> (4, 16)
    # >>> (5, 25)
    # >>> (6, 36)
    # >>> (7, 49)
    # >>> (8, 64)

```

## Internal Packages
* random - A series of functions for generating random numbers.
* math - A series of mathematical functions.
* os - A series of functions that allow developeres to interact with the operating systems, such as navigating through folders, or checking paths.
* time - A series of functions that allow developers to interact with time.
* sys - A series of functions that allow developers to interact  with the system.
* pickle - A series of functions that allow developers to interact to save and load python variables as files.
* csv - A series of functions that allow developers to read and interact with csv files.
* json - A series of functions that allow developers to read and interact with json files.

## External Packages
* matplotlib - A library for visualizing data and plotting graphs.
* numpy - A library for managing arrays and mathematical matrix operations.
* pandas - A math and statistics library for python. 
* pillow - A image creating and manipulation library.
* pytorch - A machine learning library for python. 
* sklearn - A math and statistics library for python. 
* tensorflow - A machine learning and deep learning library for python.
* tkinter - A module for developing windowed GUI applications for python.