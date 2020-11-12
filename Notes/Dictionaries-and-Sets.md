# Dictionaries and Sets

## Sets
A set is a simple data structure that contains a series of data much like a list, but a set will automatically remove duplicate entries. A important note here is that sets are non-indexable since the order of the elements is not important, but you can still iterate through them.

```python
    # A basic example set
    sets = {'element1', 'element2', 'element1'}
    print(sets)

    # Convert a list to a set
    countries = ['America', 'England', 'Scotland', 'England']
    contriesSet = set(countries)
```

## Dictionary
A dictionary is another simple data structure that uses key-value pairs. This allows for dictionaries to be indexable to retrieve the data. You can access data from the structure by using the key name in brackets.

```python
    # Creating a Dictionary
    dictionary = {"name":"Jackson", "age":23, "gender":"Male"}

    # Accessing Values
    name = dictionary["name"]
```