# Practice Set 4
# INFO-I211 - Spring 2023

"""
Overview
========

Erika and Matt are planning a "cheeses of the world" lunch.

But oh no! Their `cheeses.txt` file was corrupted.
Cheeses were duplicated, and there appear to be tabs at the
beginning of most lines:

```
    roquefort, france
roquefort, france
        mozzarella, italy
epoisses, france
            mozzarella, italy
```

This will take hours to fix this by hand 😟

We need to know which cheeses come from each country.
While Matt drives to Jungle Jim's International Market,
help Erika read the file, process it, and print something
where the countries are in alphabetical order, and the
cheeses from each country are also in alphabetical order:

```
france:
    epoisses
    roguefort
italy:
    mozzarella
```

We will be tight on time, so we should also direct Matt
based on which countries have the most cheeses:

```
[('france', 2), ('italy', 1)]
```

Practice writing *functions* that take an input
and `return` an output. When completed, all of your functions
should work together to fix the input file.

What to submit
==============

Rename `ps4.py` to `{username}_ps4.py` and submit the
Python script on Canvas.

For example, Alexander would submit `hayesall_ps4.py` on Canvas.

Tips
====

1. Practice iterative development. If you see this:

```
# Implement `list_to_string()` which takes a list of integers
# like [1, 2, 3] and returns "1 2 3".
def list_to_string(input_list):
    pass
```

... then you might implement + test the function works like this:

```
def list_to_string(input_list):
    return str(input_list)[1:-1].replace(", ", " ")

print(list_to_string([1, 2, 3]))
```

2. Make sure to *return* values from your function,
   *printing* values is not the same as returning them!
3. When you're confident that your functions are correct,
   clean up any debugging code you wrote. Your final
   implementation should *only* print the result of PS 4.6
"""
from operator import itemgetter

# PS 4.1
# ------
# `safe_load_file` takes a string representing the name of a file
# as an input. If the file exists, return the file's contents as a string.
# If the file does not exist, return the empty string.
#
# Examples:
# >>> print(safe_load_file("cheeses.txt"))
# roquefort, french\nmozzarella, italy\nepoisses, france ...
#
# >>> print(safe_load_file("C:\\User\\notes.txt"))
#           <--- nothing shown because the empty string was printed
#
# Hint:
# - Use `try` and `except FileNotFoundError` to catch the error.
# - The `os` module is an alternative way to approach this.

def safe_load_file(file_path: str) -> str:
    try:
        # if files does exist, open file and print as string
        with open(file_path, 'r') as file:
            data = file.read()
            return data
    # if file does not exist, print empty string
    except FileNotFoundError:
        return ''

# test print statement 
# print(safe_load_file('cheeses-corrupted.txt'))


# PS 4.2
# ------
# Implement `to_nested_list`, which takes a string as input and
# converts it to a list-of-lists. Assume the input is a
# newline-separated string, may contain tabs, and each line
# contains two values separated by a comma and a space (", ").
#
# Example:
# >>> to_nested_list("\t\troquefort, french\nroquefort, french")
# [['roquefort', 'french'], ['roquefort', 'french']]

def to_nested_list(string_data):
    # cleaning up the data
    data = string_data.split('\n')
    # list comprehension to make it print on one line
    return [i.strip(' \t').split(', ') for i in data if i != '']

# test print statement
# print(to_nested_list("\t\troquefort, french\nroquefort, french"))


# PS 4.3
# ------
# Write `nested_lists_to_dict`, which takes a "list of list of strings"
# where each inner list has a (value, key) pair. Return a dictionary
# where each key maps to a list of *unique* values.
#
# Examples:
# >>> nested_lists_to_dict([["feta", "greece"], ["feta", "greece"]])
# {'greece': ['feta']}
# >>> nested_lists_to_dict([["roquefort", "france"], ["roquefort", "france"], ["feta", "greece"], ["brie", "france"]])
# {'france': ['roquefort', 'brie'], 'greece': ['feta']}

def nested_lists_to_dict(input_lol):
    # create empty dictionary 
    cheese_dict = {}
    for i in input_lol:
        # unpacking the data
        cheese, country = i[0], i[1]
        if country not in cheese_dict: 
            # replace value
            cheese_dict[country] = [cheese]
        elif cheese not in cheese_dict[country]:
            # add value 
            cheese_dict[country].append(cheese)
    # return dictionary
    return cheese_dict

# test print statement
# print(nested_lists_to_dict([["roquefort", "france"], ["roquefort", "france"], ["feta", "greece"], ["brie", "france"]]))
        

# PS 4.4
# ------
# Implement `format_dict_of_lists` which takes a dictionary of lists,
# sorts the keys in the dictionary, and returns a string. The
# keys should be sorted, and the values should be sorted.
#
# >>> print(format_dict_of_lists({'france': ['roquefort', 'brie'], 'greece': ['feta', 'halloumi']}))
# france:
#   brie
#   roquefort
# greece:
#   feta
#   halloumi
#
# Hint:
# You can use '\t' to create a tab, and a `\n` to create
# a newline. Make sure this function *returns* a string,
# *printing* the output directly will cause an error!

# **key = countries | value = cheese**
def format_dict_of_lists(input_dol):
    # create empty string
    my_string = ''
    # convert to list
    countries = list(input_dol.keys())
    # sort keys
    countries.sort()
    for country in countries:
        my_string = my_string + country + ':\n' 
        cheeses = input_dol[country]
        # sort values
        cheeses.sort()
        for cheese in cheeses:
            # formatting using tab
            my_string = my_string + '\t' + cheese + '\n'
    # return string value 
    return my_string

# test print statement
#print(format_dict_of_lists({'france': ['roquefort', 'brie'], 'greece': ['feta', 'halloumi']}))


# PS 4.5
# ------
# Write `summarize_dict_of_lists`, which takes a dictionary mapping
# strings to lists, and returns a list of tuples representing the
# key and length of each list. The tuples be should be sorted from
# highest to lowest.
#
# Example:
# >>> summarize_dict_of_lists({'france': ['roquefort', 'brie'], 'greece': ['feta']})
# [('france', 2), ('greece', 1)]

def summarize_dict_of_lists(input_dol):
    # create empty list 
    my_list = []
    for countries, cheese in input_dol.items():
        # get length of list of values
        cheese_len = len(cheese)
        # add to list as tuple
        my_list.append((countries, cheese_len))
        # sort the list
        sorted_list = sorted(my_list, key=itemgetter(1), reverse=True)
    # return list
    return sorted_list

# test print statement  
# print(summarize_dict_of_lists({'france': ['roquefort', 'brie'], 'greece': ['feta']}))


# PS 4.6
# ------
# Uncomment the following `if __name__ == "__main__` lines
# with CTRL + /        or        ⌘ + /
# Running this file using the "Run Python File" button
# (triangle in the top right), or invoking from the terminal
# with `python ps4.py` should now display the cheeses.

if __name__ == "__main__":
    cheeses = nested_lists_to_dict(to_nested_list(safe_load_file("cheeses-corrupted.txt")))
    print(format_dict_of_lists(cheeses))
    print(summarize_dict_of_lists(cheeses))
