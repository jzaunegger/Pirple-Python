# Classes
Classes are data structures that carry thier own variable and functions. Classes in python use the keyword 'class' followed by the class name folled with a colon. Each class also needs a constructor to create a instance of that class. The constructor function will take in the input parameters to create object attributes. Those attributes can be accessed from other functions in the same class. It is important to note that each attribute and function needs to reference the keyword 'self', to reference itself through out the class. Classes are like blueprints for how an data structure should behave. 

```python

    # Create the base class
    class Calc:

        # Constructor function
        def __init__(self, x, y):
            self.x = x
            self.y = y 

        # Add function
        def add(self):
            return self.x + self.y
            
        # Add function
        def sub(self):
            return self.x - self.y

        # Add function
        def mul(self):
            return self.x * self.y

        # Add function
        def div(self):
            return self.x / self.y

    newClass = Calc(10, 5)
```

## Inheritance
Inheritance is a concept related to classes using other classes. With inheritance there is a base or parent class that had normal attributes and methods, but also contains sub or child classes that have thier own attributes and methods. It is a method for structuring code to be more useable.

```python

    # Create the parent class
    class BaseLayer:
        def __init__(self):
            self.x = 0
            self.y = 0

        # Create a child class
        class CharBase(BaseLayer):   
            def __init__(self):
                BaseLayer.__init__(self)

        # Create a child class
        class Constellation(BaseLayer):   
            def __init__(self):
                BaseLayer.__init__(self)

        # Create a child class
        class MaurerRose(BaseLayer):   
            def __init__(self):
                BaseLayer.__init__(self)

        # Create a child class
        class Rose(BaseLayer):   
            def __init__(self):
                BaseLayer.__init__(self)

        # Create a child class
        class Rosette(BaseLayer):   
            def __init__(self):
                BaseLayer.__init__(self)

        # Create a child class
        class Spiral(BaseLayer):   
            def __init__(self):
                BaseLayer.__init__(self)
                
        # Create a child class
        class Star(BaseLayer):   
            def __init__(self):
                BaseLayer.__init__(self)
```

