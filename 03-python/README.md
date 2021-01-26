# Python

Python has the following data types built-in by default, in these categories:

* Text Type: str
* Numeric Types: int, float, complex
* Sequence Types: list, tuple, range
* Mapping Type: dict
* Set Types: set, frozenset
* Boolean Type: bool
* Binary Types: bytes, bytearray, memoryview

Variables:

* Variables are containers for storing data values.
* Variables do not need to be declared with any particular type, and can even change type after they have been set.

Variables in Python:

* Utilize lower_case_with_underscore (for convention purposes)
* Do not start the name of variables with numbers, otherwise they are allowed
* Special characters are not allowed, except for "_"

Python Relational Operators:

| Operator | Name | Example | 
| --- | --- | --- | 
| == | Equal | x == y |
| != | Not equal | x != y |
| > | Greater than | x > y |
| < | Less than | x < y |
| >= | Greater than or equal to |	x >= y |
| <= | Less than or equal to | x <= y | 

Logical Operators:

| Operator | Description | Syntax |
| --- | --- | --- 
| and | Logical AND: True if both the operands are true | x and y |
| or | Logical OR: True if either of the operands is true | x or y |
| not | Logical NOT: True if operand is false | not x |
```Python
# Examples of Logical Operator 
a = True
b = False
  
# Print a and b is False 
print(a and b) 
  
# Print a or b is True 
print(a or b) 

# Print not a is False 
print(not a) 
```

```Python
Output:

False
True
False
```

Strings

* Strings in python are surrounded by either single quotation marks, or double quotation marks.
  * 'hello' is the same as "hello".
* Multiline Strings
* You can assign a multiline string to a variable by using three quotes:

``` Python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
```
* **Strings are Arrays**
  * Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
  * Since strings are arrays, we can loop through the characters in a string, with a for loop.
* Common operations:
  * Replace character: replace()
  * Make a character uppercase or lowercase: upper() and lower()
  * Check if character starts or ends with characters: startswith() and endswith()
  * Removing spaces and characters: strip(), lstrip(), rstrip()
  * Getting characters by index: [0:2], [:2]
  * Use operators: IN and NOT IN

String Manipulation:
* Concatenation
  * Only between strings
* Interpolation:
  * Markers Method (%d, %s and %f)
    * %d - Int
    * %f - Float
    * %s - String
  * Format Method
    * print ('My name is {}'.format(name))
  * F-string Method
    * Only on Python 3.6+
## Notes

* Extra reading:
  * [W3 - Python Tutorial](https://www.w3schools.com/python/python_intro.asp)
  * [Python Docs - Python Tutorial](https://docs.python.org/3/tutorial/index.html)
  * [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
  * [PEP 8](https://www.python.org/dev/peps/pep-0008/)
    * Indentation: 4 spaces
    * Tabs and spaces do not mix
    * Max size of line: 79 chars
    * Blank lines: Use with care
    * Import should be used in separate lines
  * [Data Types](https://www.w3schools.com/python/python_datatypes.asp)
  * [Variables](https://www.w3schools.com/python/python_variables.asp)
  * [Arithmetic Operators](https://www.geeksforgeeks.org/python-operators/)
  * [Strings](https://www.w3schools.com/python/python_strings.asp)
  * [Modify Strings](https://www.w3schools.com/python/python_strings_modify.asp)
  * [Concatenate Strings](https://www.w3schools.com/python/python_strings_concatenate.asp)
  * [Format Strings](https://www.w3schools.com/python/python_strings_format.asp)
  * [String Methods](https://www.w3schools.com/python/python_strings_methods.asp)
  * [User input](https://www.w3schools.com/python/python_user_input.asp)
  * [While Loops](https://www.w3schools.com/python/python_while_loops.asp)
  * [Conditions](https://www.w3schools.com/python/python_conditions.asp)
    * The form if-if-if tests all conditions, whereas the if-elif-else tests only as many as needed: if it finds one condition that is True, it stops and doesn't evaluate the rest. In other words: if-elif-else is used when the conditions are mutually exclusive.
  * [Lists](https://www.w3schools.com/python/python_lists.asp)
    * [List Methods](https://www.programiz.com/python-programming/methods/list)
  * 