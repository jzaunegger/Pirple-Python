# Lists
* Lists, or arrays in other languages are simple data structures that allow you to assign a series of values to an object, and access these values using indicies.
* Lists come with a variety of methods attached to them to automate common operations and proccesses. 
* Each entry of a list does not have to be the same type, you can have mixed types. List elements can also be objects or other lists. 
* Indicies that are negative will retrieve elements starting at the end of the list. Otherwise, a given index will start counting at zero.
* Using a colon (list[n:m]) will return a list of the given elements from index n up to but not including m. If n is not given, the list will return n up to and not including m, and if m is not given the list will go from n to the last index of the list.

* Example
    ```python
        # Examples of Lists
        testList = ["element1", "element2", "elementN"]
        testList.append("Jackson")

        testList2= ["Test1", "Test2"]
        testList.append(testList2)

        # Example Outputs
        testList[3] >>>  "Jackson"
        testList >>> '["element1", "element2", "elementN", "Jackson"]'
        testList[0:2] >>> '["element1", "element1"]'
        testList[3][0] >>> "Test1"

    ```

## Common List Methods
* .append()             : Add a new item to the last index of the list.
* .pop(i)               : Remove the element at the given index.
* .remove(elem)         : Removes the given element from the list.
* .clear()              : Clear all elements from a list.
* .copy()               : Returns a copy of the list.
* .count()              : Returns the size of the list.
* .insert(i, element)   : Inserts a given element and the given index.
                            Every element after the index will shift to 
                            the right.
* .reverse()            : Reverse the elements in the list.