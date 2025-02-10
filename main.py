## Variables
## =================================
# The equal sign (=) is used to assign a value to a variable

spam = 1  # and this is a comment
spam_txt = "one"
text = "# This is not a comment because it's inside quotes."

## Data Types
## ================================= 
## Numbers
## ---------------------------------
# Using Python as a Calculator!
2 + 2
# 4

2 * 2
# 4

8 / 5 # division always returns a floating-point number
# 1.6

17 / 3 # classic division returns a float
# 5.6666...

17 // 3  # floor division discards the fractional part
# 5

17 % 3  # the % operator returns the remainder of the division
# 2

5 ** 2  # 5 squared
# 25

2 ** 7  # 2 to the power of 7
# 128

# Tip: In interactive mode, the last printed expression is assigned to the variable _.
_ * 2
# 256

## Create a variable and assign a number
weight = 20
height = 30 * 2
area = weight * height
area
# 1200

# Number types
# The built-in function "type()" returns the type of an object:
type(area)
# <class 'int'>

type(area / 7)
# <class 'float'>

# In addition to "int" and "float", Python supports other types of numbers, 
# such as "Decimal" (more or more precise calculations than float) 
# and "Fraction" (eg. 3/4 + 7/8 = 13/8). 
# Python also has built-in support for complex numbers, and uses the j or J suffix to indicate the imaginary part (e.g. 3+5j).

####
#from fractions import Fraction
#Fraction(1, 2) + Fraction(7, 8)
####

# Note: Numbers are immutable (not modifiable), non-subscriptable (non-sliceable), and cannot be concatenated (glued together).
# Therefore, there is no method for numbers!

## Text
## ---------------------------------
'spam eggs'  # single quotes
# 'spam eggs'

"Paris rabbit got your back :)! Yay!"  # double quotes
# 'Paris rabbit got your back :)! Yay!'

"It doesn't"
#"It doesn't"

'1975'  # digits and numerals enclosed in quotes are also strings
#'1975'

# String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''.
print('''This is line one
and two
and more ...
''')

## Create a variable and assign a text (string)
p = 'Py'
c = 'Coding'

## Text type
type(p)
# <class 'str'>

# Note: Strings are immutable (not modifiable), subscriptable (sliceable), and can be concatenated (glued together).
# Therefore, there are many predefined methods for strings.

# Concatenate (glued together)
p + 'thon'
# 'Python'

p * 2
# 'PyPy'

p + ' ' + c
# 'Python Coding'

# Subscriptable (sliceable)
p[0]
# 'P'

p[0:2] # or p[:2]
# 'Py'

p[2:]
# 'thon'

p[-1]
# ???

p[::2] # from:to:step, default step is 1 
# 'Pto'

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

p[::-1]
# ???

# The built-in function "len()" returns the length of a string:
len(p)
# 6

# String methods
p.capitalize()
p.upper()
p.lower()
p.index('P')
p.find('P')
p.index('p')
p.find('p')
','.join(p)
p.split('t')
p.replace('P', 'M')
p.count('P')
p.center(20, '-')

## Qzzzzz
p = "Python"
c = "Coding"
p = p + c
p
# ???

p = "Python"
c = "Coding"
p += c
p
# ???

p = "Mython"
p[0] = "P"
# ???

## Other types
## ---------------------------------
type(True)
# <class 'bool'>

type(False)
# <class 'bool'>

type(None)
# <class 'NoneType'>

type(true)
# ???

## Lists
## ---------------------------------
# Python knows a number of compound data types, used to group together other values. 
# The most versatile is the "list", which can be written as a list of comma-separated values (items) between square brackets. 
# Lists might contain items of different types, but usually the items all have the same type.

squares = [1, 4, 9, 16, 25]

type(squares)
# <class 'list'>

# Note: Lists are mutable (modifiable), subscriptable (sliceable), and can be concatenated (glued together).
# Therefore, there are many predefined methods for lists.

# Subscriptable (sliceable) 
squares[1]
# ???

squares[-1]
# ???

squares[2:]
# ???

# Concatenate (glued together)
squares + [36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares + ['one', 'four', '9', 100, True]
# ???

# It is possible to nest lists (create lists containing other lists), for example:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
# [['a', 'b', 'c'], [1, 2, 3]]

x[0]
# ['a', 'b', 'c']

x[0][1]
# ???

# Mutable (modifiable)
cubes = [1, 8, 27, 65, 125]
id(cubes)

cubes[3] = 64
# ???
id(cubes)

# List methods
cubes.append(216)
cubes
cubes.index(216)
cubes.reverse()
cubes
cubes.sort()
cubes
cubes.remove(216)
cubes

# Qzzzzz
rgb = ["Red", "Green", "Blue"]
rgb_copy = rgb  # a copy of rgb list!
rgb_copy.append("Alpha")
rgb_copy
# ???
rgb
# ???

id(rgb) == id(rgb_copy) # they reference the same object
# True

rgb = ["Red", "Green", "Blue"]
correct_rgb_copy = rgb[:]
correct_rgb_copy.append("Alpha")
correct_rgb_copy
# ???
rgb
# ???

id(rgb) == id(correct_rgb_copy)

