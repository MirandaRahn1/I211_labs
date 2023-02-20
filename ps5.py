# Practice Set 5
# INFO-I 211 - Spring 2023

"""
Matt and Erika have a friend in the biology department who studies turtles
and supplied them with detailed records in a `.csv` file.

- `turtles_subset.csv`: a subset of 10 turtles
- `turtles_all.csv`: 3929 rows of turtle data

The friend did not go into details: but apparently they've been *tearing
their hair out* trying to analyze this data in Excel.

Turtles squirm when you try to measure their shells. So the "length"
column contains a string of numbers representing the multiple
measurements that had to be taken for each turtle:

```
  species     sex               length  age
-------------------------------------------
Softshell  female  11.2 11.3 11.3 11.4   21
Softshell  female       11.3 11.2 11.2   11
  Spotted  female          5.2 5.1 5.1   60
  Spotted    male              3.8 3.7   42
Softshell    male              8.9 8.6    9
  Spotted    male          3.7 3.8 3.7   38
Softshell    male          9.3 9.0 9.3   14
Softshell  female       11.8 11.8 11.8   32
  Spotted  female  4.4 4.3 4.6 4.8 4.7   37
Softshell    male          8.9 9.3 9.1   14
```

The *true* shell measurement is probably near the average of the recorded
measurements. At some point we'll want to take the mean of values in
the "length" column:

```
"3.5 3.5"                   -->  3.5
"11.2 11.2 11.1 11.1"       --> 11.149
"9.2 9.6 9.5 9.5 9.2 9.4"   -->  9.4
"9.0 9.2 9.3"               -->  9.2
```

We've written some starter code, but we need your help finishing the
analysis.

Specifically: we need to compute summary statistics like the minimum,
maximum, and mean values for turtle ages and shell lengths.

**Tips**:

Develop and debug your functions using the `turtles_subset.csv`. When you're
confident with your solution, apply your functions to the `turtles_all.csv`
to complete the analysis!
"""


# PS 5.0
# ------
# The first two functions are *nearly* free! We've seen something
# like `read_csv` in the lecture slides, and we've included a
# `print_table` function here. `read_csv` should use `csv.DictReader`
# and return a list of dictionaries.
#
# ```
# table = read_csv("turtles_subset.csv")
# print_table(table)
# ```
#
# The underlying table should still be our "List of Dictionaries" we've
# been practicing with, but `print_table` will format the output to
# make it easier to interpret.


def read_csv(file_name):
    pass


def print_table(table):
    """Print a formatted table from a list of dictionaries.
    This assumes that every dictionary in the list contains the same keys.
    """

    def format_table(table):
        """table->string: table length >= 1"""
        # Initialize a "max length" list based on the length of row 0 keys.
        mlen = [len(k) for k in table[0].keys()]

        # Update `mlen` based on the maximum length of values in each row.
        for row in table:
            for i, v in enumerate(row.values()):
                mlen[i] = max(mlen[i], len(str(v)))

        # Build a format string and use it format the table to a string.
        tform = "".join("  {:>" + f"{i}" + "}" for i in mlen)
        out = [tform.format(*table[0].keys())]
        out += ["-" * (sum(mlen) + (2 * len(mlen)))]
        out += [tform.format(*row.values()) for row in table]
        return "\n".join(out)

    if not table:
        print("Empty Table.")
    elif len(table) > 10:
        print(format_table(table[:10]))
        print(f"  ... {len(table)} total rows")
    else:
        print(format_table(table))


# PS 5.1
# ------
# Our `read_csv` function returns a list of dictionaries where every
# key and value is a string. This means that "age" values are all strings.
# Implement `convert_column_to_floats`, which takes a table and the name
# of a column as input, and converts the value in every row to a float.
#
# This function should *not* need to return anything! It should iterate
# over rows in the table, converting values to floats.
#
# Hint: When you run the following lines, can you see the difference
# between the original version of the table, and the table after you
# convert the age values to floats?
#
# ```
# table = read_csv("turtles_subset.csv")
# print_table(table)
#
# convert_column_to_floats(table, "age")
# print_table(table)
# ```


def convert_column_to_floats(table, column_name):
    pass


# PS 5.2
# ------
# Write a function `extract_floats` which takes a string as input
# (e.g. "11.2 11.2 11.1 11.1") and returns a list of floats.
#
# >>> extract_floats("11.2 11.2 11.1 11.1")
# [11.2, 11.2, 11.1, 11.1]


def extract_floats(input_string):
    pass


# PS 5.3
# ------
# There are a huge number of potential "edge cases" that may come up with
# our implementation of `extract_floats`.
#
# Test how your implementation behaves with the following examples.
# What output does each produce? Do they seem appropriate?
#
# ```
# extract_floats("1.9 kilograms")
# extract_floats("1, 2, or 3")
# extract_floats("88mph")
# extract_floats("5 pounds 11 ounces")
# extract_floats("1 year and 6 months")
# extract_floats("+1 (555) 555-5555")
# extract_floats("6e 61 6d 65")
# ```
#
# Pick one of these cases and describe an output that may be more appropriate.
# Can you frame a solution as first "detecting a pattern" and "extracting?"
# (e.g. "Phone numbers are often formatted as ___, therefore ___")
# Add pseudocode or describe a potential solution, you do not have to implement
# your idea.
#
# Looking ahead:
# Later, we'll see the "regular expressions" (re) module as a way to
# formalize some of these problems (https://docs.python.org/3/library/re.html)


"""
(Describe your thoughts here...)
"""


# PS 5.4
# ------
# Implement the `add_estimated_length_column` function, which takes our
# `table` of data, and adds a new key "estimated_length" to each dictionary
# in the list. "estimated_length" represents the mean of the "length" values.
#
# - Use your `extract_floats` implementation
# - Use the "length" key in each dictionary
# - `from statistics import mean` might be helpful, but is not required
# - Round the "estimated_length" result to 1 decimal place
# - This function should *modify* each dictionary, *therefore* the function
#   does not need to return anything.
#
# ```
# table = read_csv("turtles_subset.csv")
# add_estimated_length_column(table)
# ```


def add_estimated_length_column(table):
    pass


# PS 5.5
# ------
# There are three function stubs below: `column_mean`, `column_min`, and
# `column_max`. Implement all three.
#
# Each takes our `table` and the name of a `column` as input, and should
# return the mean, min, or max of the values in a column.
#
# ```
# table = read_csv("turtles_subset.csv")
# convert_column_to_floats(table, "age")
# print(column_min(table, "age"))           # Should be:  9.0
# print(column_max(table, "age"))           # Should be: 60.0
# print(column_mean(table, "age"))          # Should be: 27.8
# ```


def column_mean(table, column):
    pass


def column_min(table, column):
    pass


def column_max(table, column):
    pass


# PS 5.6 - Complete the Analysis!
# -------------------------------
# We should have everything we need to answer the original question: what are
# the minimum, maximum, and average ages and lengths of turtles in the dataset?
#
# You should be able to un-comment the following main module to complete the
# analysis.
#
# if __name__ == "__main__":
#     for dataset in ("turtles_subset.csv", "turtles_all.csv"):
#         table = read_csv(dataset)
#
#         add_estimated_length_column(table)
#         convert_column_to_floats(table, "age")
#
#         ages = (
#             column_min(table, "age"),
#             column_max(table, "age"),
#             column_mean(table, "age"),
#         )
#         lengths = (
#             column_min(table, "estimated_length"),
#             column_max(table, "estimated_length"),
#             column_mean(table, "estimated_length"),
#         )
#         print(dataset + ":")
#         print(f"Turtle Ages    | Min {ages[0]}, Max {ages[1]}, Mean {ages[2]}")
#         print(f"Turtle Lengths | Min {lengths[0]}, Max {lengths[1]}, Mean {lengths[2]}")
#         print("---")
