# object Types and Data types

- Numbers : 123, 120.50, 3+4j, 0b1010, 0o12, 0xA, Deciaml(10), Fraction(1, 3)
- Strings : 'Hello', "World", '''This is a string''', """This is also a string""", r'Raw String', f'Formatted String {variable}'
- Lists : [1, 2, 3], ['a', 'b', 'c'], [1, 'a', 3.14], [],[1, [2, 3], 4]
- Tuples : (1, 2, 3), ('a', 'b', 'c'), (1, 'a', 3.14), (), (1, [2, 3], 4),(1,'spam',4,u), tuple('spam')
- Dictionaries : {'name': 'Alice', 'age': 30}, {1: 'one', 2: 'two'}, {}, dict(name='Alice', age=30)
- Sets : {1, 2, 3}, {'a', 'b', 'c'}, {1, 'a', 3.14}, set()
- File objects : open('file.txt', 'r'), open('file.txt', 'w'), open('file.txt', 'a')
- Booleans : True, False
- None : None
- Functions : def my_function(): pass, lambda x: x + 1
- Modules : import math, import os, import sys
- classes : class MyClass: pass, class Person: def __init__(self, name): self.name = name
- Advance : Decorators, Generators, Context Managers, Coroutines, Async/Await,Iterators,Metaprogramming , Comprehensions, Regular Expressions, Exception Handling, File Handling, Object-Oriented Programming (OOP), Functional Programming, Data Structures (Lists, Tuples, Sets, Dictionaries), Algorithms (Sorting, Searching), Libraries (NumPy, Pandas, Matplotlib), Web Development (Flask, Django), Data Science (Scikit-learn, TensorFlow), Machine Learning (Keras, PyTorch), Natural Language Processing (NLTK, SpaCy), Computer Vision (OpenCV), Database Connectivity (SQLite3, SQLAlchemy), Testing (unittest, pytest), Debugging (pdb), Version Control (Git), Virtual Environments (venv, conda)

[]:- Brackets for lists
():- Parentheses for tuples
{}:- Curly braces for sets and dictionaries 


# For Helping Use Dir() and Help() functions
- dir() : Returns a list of valid attributes of the object.
- help() : Provides detailed information about an object, including its methods and attributes.
# Example:
my_list = [1, 2, 3] 
print(dir(my_list))
print(help(my_list))

len(my_list) # Output: 3
my_list.append(4)
print(my_list) # Output: [1, 2, 3, 4]           

myD = {'one':"leamontea", 'second':'gingertea','comic':'naagraj'}

print(myD.keys()) # Output: dict_keys(['one', 'second', 'comic'])
print(myD.values()) # Output: dict_values(['leamontea', 'gingertea', 'naagraj'])
print(myD.items()) # Output: dict_items([('one', 'leamontea'), ('second', 'gingertea'), ('comic', 'naagraj')])          

myTup = (4,4,2,4,5)
print(myTup.count(4)) # Output: 3
print(myTup.index(5)) # Output: 4
len(myTup) # Output: 5
myTup[1] # Output: 4


username = "chaiaurcode"
print(username[0]) # Output: 'c'
print(username[1]) # Output: 'h'
print(username[-1]) # Output: 'e'
print(username[0:5]) # Output: 'chaia'  
username[0] = 'A' # This will raise a TypeError because strings are immutable

dir(username) #['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# Example: 

import sys
sys.getrefcount(34234)  o/p 3
sys.getrefcount('hitesh')  0/p 3

a = 5
b = 2 
a = a + 2
o/p = 7

listOne = [1,2,3,4]
listTwo = listOne
listOne = [1,2,3,4]
listOne[0] = 33
print(listOne)  o/p [33,2,3,4]


p1 = [6,7,8]
p2 = p1
p2 = [1,2,3]
p1[0] = 44
print(p1)  o/p [44,7,8]
p2[0] = 22
print(p2) = [22,2,3]

# Copy Feature 

- h1 = [1,2,3,4]
- h2 = h1[:]
- print(h1)  o/p [1,2,3,4]
- 
- h1[0] = 55
- h2[0] = 33
- 
- print (h1) o/p [55,2,3,4]
- print (h2) o/p [33,2,3,4]
 # Example1:
- 
- import copy
- h2 = copy.copy(h1)
- 
- print(h2) = o/p [55,2,3,4]
-  
- h2 = copy.deepcopy(h1) 
- 
- n = [1,2,3,4]
- m=n
- print(m)  o/p [1,2,3,4]
- print(n)  o/p [1,2,3,4]
- 
- m == n  o/p true
- m is n  o/p true
 # Example2:
- n = [1,2,3,4]
- m = [1,2,3,4]
- 
- m == n  o/p true
- m is n  o/p false

# Numbers are immutable, while lists and dictionaries are mutable. When you assign a new value to a variable that references an immutable object, a new object is created in memory. However, when you modify a mutable object, the same object is updated in memory.


# Numbers : int, float, complex, bool, Decimal, Fraction

# Example:
- a = 10
- b = 3.14
- c = 1 + 2j
- d = True
- e = Decimal('10.5')
- f = Fraction(3, 4)


- >>> repr('chai')
"'chai'"
- >>> str('chai')
'chai'
- >>> print('chai')
chai

- >>> 1 < 2
True
- >>> 1 > 2
False
- >>> 5.0 == 5.0
True
- >>> 4.0 != 5.0
True
- >>> x =2
- >>> y = 3
- >>> z = 4
- >>> x,y,z
(2, 3, 4)
- >>> x < y < z
True
- >>> x < y and y < z
True
- >>> x < y and y < z
True
- >>> x < y or  y < z 
True
- >>> 1 == 2 < 3
False
- >>> 1 == 2 and 2 < 3  
False

- >>> import math
- >>> math.floor(3.5)
3
- >>> math.floor(-3.5) 
-4
- >>> math.floor(3.6)  
3
- >>> math.floor(-3.9) 
-4
- >>> math.trunc(-3.9) 
-3
- >>> math.trunc(3.9)  
3
- >>> math.trunc(2.8) 
2
- >>> math.trunc(-2.8) 
-2
- >>> 9999999999999999999999 + 1
10000000000000000000000
- >>> 9999999999999999999999 * 2.1
2.1000000000000002e+22
- >>> 2 ** 200
1606938044258990275541962092341162602522202993782792835301376
- >>> 2 + 1j
(2+1j)
- >>> 2 + 1j * 3
(2+3j)
- >>> (2 + 1j) * 3 
(6+3j)
- >>> 0o20
16
- >>> 0xFF
255
- >>> 0b1000
8
- >>> oct(64)
'0o100'
- >>> hex(64)
'0x40'
- >>> bin(64)
'0b1000000'
- >>> bin(64A)
  File "<stdin>", line 1
    bin(64A)
         ^
SyntaxError: invalid decimal literal
- >>> bin(64)  
'0b1000000'
- >>> int(64) 
64
- >>> int('64', 8 )
52
- >>> int('64', 16 ) 
100
- >>> int('10000', 2 )  
16
- >>> x = 1
- >>> x << 2
4
- >>> x >> 2
0
- >>> import random
- >>> random.random()
0.554904150318123
- >>> random.random()
0.16633324511759695
- >>> random.randint(1, 10)
10
- >>> random.randint(1, 10)
8
- >>> random.randint(1, 10)
9
- >>> l1 = ['lemon', 'masala', 'ginger', 'mint']
- >>> random.choice(l1)
'lemon'
- >>> random.choice(l1)
'masala'
- >>> random.choice(l1)
'masala'
- >>> random.shuffle(l1)
>>> l1
['lemon', 'masala', 'ginger', 'mint']
- >>> random.shuffle(l1)
- >>> l1
['masala', 'ginger', 'mint', 'lemon']
- >>> 0.1 + 0.1 + 0.4
0.6000000000000001
- >>> 0.1 + 0.1 + 0.1   
0.30000000000000004
- >>> 0.1 + 0.1 + 0.1 - 0.3 
5.551115123125783e-17
- >>> (0.1 + 0.1 + 0.1) - 0.3 
5.551115123125783e-17
- >>> from decimal import Decimal 
- >>> Decimal('0.1') + Decimal('0.') + Decimal('0.1')
Decimal('0.2')
- >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') 
Decimal('0.3')
- >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')
- >>> from fractions import Fraction
- >>> myFra = Fraction(2, 8)
- >>> myFra
Fraction(1, 4)
- >>> myFra = Fraction(2, 7) 
- >>> myFra
Fraction(2, 7)
- >>> setone = {1,2,3,4}
- >>> setone
{1, 2, 3, 4}
- >>> setone & {1, 3}
{1, 3}
- >>> setone | {1, 3} 
{1, 2, 3, 4}
- >>> setone | {1, 3, 7} 
{1, 2, 3, 4, 7}
- >>> setone
{1, 2, 3, 4}
- >>> setone - {1,2,3,4}
set()
- >>> type({})
<class 'dict'>
>>> type(True)
<class 'bool'>
- >>> True == 1
True
- >>> False == 0 
True
- >>> True is 1
-<stdin>-130:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
- >>> True 
True
- >>> True + 4
5
- >>> False + 4
4

# STRINGS :- str, bytes, bytearray
# Strings are immutable, which means that once a string is created, it cannot be modified. When you perform an operation that seems to modify a string, it actually creates a new string object in memory. For example:

# Example:

- name = "chai aur code"
- name[0] = 'C'  # This will raise a TypeError because strings are immutable
- name = "Chai aur code"  # This creates a new string object in memory  

- >>> chai = "Leamon Chai "
- >>> chai 
'Leamon Chai '
- >>> print(chai)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    Print(Chai)
    ^^^^^
NameError: name 'Print' is not defined. Did you mean: 'print'?
- >>> print(chai)
Leamon Chai 
- >>> chai = "Masala chai"
- >>> chai[0]      
'M'
- >>> first_chr = chai[0]
- >>> print(first_chr)
M
- >>> chai 
'Masala chai'
- >>> slice_chai = chai[0:6
... ]
- >>> 
- >>> slice_chai = chai[0:6]
- >>> print(slice_chai)
Masala
- >>> chai[-1]
'i'
- >>> num_list = '0123456789'
- >>> num_list[:]
'0123456789'
- >>> num_list[3:] 
'3456789'
- >>> num_list[:7]  
'0123456'
- >>> num_list[0:7:2] 
'0246'
- >>> num_list[0:7:3] 
'036'
- >>> num_list[0:7:-1] 
''
- >>> num_list[0:7:0]  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    num_list[0:7:0]
    ~~~~~~~~^^^^^^^
ValueError: slice step cannot be zero
- >>> chai
'Masala chai'
- >>> print(chai.lower()) 
masala chai
- >>> print(chai.upper()) 
MASALA CHAI
- >>> chai
'Masala chai'
- >>> chai = "  Masala Chai   "
- >>> print(chai)
  Masala Chai   
- >>> chai
'  Masala Chai   '
- >>> print(chai.strip())
Masala Chai
- >>> chai = "Leamon chai"
- >>> print(chai.replace("Leamon", "Ginger"))
Ginger chai
- >>> chai
'Leamon chai'
- >>> chai = "Lemon,ginger,mint,Masala"
- >>> chai
'Lemon,ginger,mint,Masala'
- >>> print(chai.split()) 
['Lemon,ginger,mint,Masala']
- >>> print(chai.split(",")) 
['Lemon', 'ginger', 'mint', 'Masala']
- >>> chai = "Masala Chai"
- >>> print(chai.find("Chai")) 
7
- >>> print(chai.find("chai")) 
-1
    print(find("Chai"))
          ^^^^
NameError: name 'find' is not defined
- >>> chai
'Masala Chai'
- >>> print(chai.find("Chai")) 
7
- >>> print(chai.find("chai")) 
-1
- >>> chai = "Masala Chai Chai Chai"
- >>> print(chai.count("Chai")) 
3
- >>> chai_type = "Masala" 
- >>> quantity = 2
- >>> order = "I ordered {} cups of {} chai"
- >>> order
'I ordered {} cups of {} chai'
- >>> print(order.format(quantity,chai_type)) 
I ordered 2 cups of Masala chai
- >>> chai_variety = ["Lemon", "Masala", "Ginger"] 
- >>> chai_variety
['Lemon', 'Masala', 'Ginger']
- >>> print("".join(chai_variety))
LemonMasalaGinger
- >>> print(" ".join(chai_variety)) 
Lemon Masala Ginger
- >>> print("-".join(chai_variety))  
Lemon-Masala-Ginger
- >>> print(", ".join(chai_variety)) 
Lemon, Masala, Ginger
- >>> chai 
'Masala Chai Chai Chai'
- >>> chai = "Masala chai"
- >>> print(len(chai))
11
- >>> chai
'Masala chai'
- >>> for letter in chai :
...     print(letter)
... 
M
a
s
a
l
a

c
h
a
i
- >>> chai = "He said, \"Masala chai is awesome"\" 
  File "<stdin>", line 1
    chai = "He said, \"Masala chai is awesome"\"
                                               ^
SyntaxError: unexpected character after line continuation character
- >>> chai = "He said, \"Masala chai is awesome\"" 
- >>> chai
'He said, "Masala chai is awesome"'
- >>> chai = "Masala\nchai"
- >>> chai
'Masala\nchai'
- >>> print(chai)\
...
Masala
chai
>>>
- >>> chai = r"Masala\nchai"
- >>> print(chai)
Masala\nchai
- >>> chai = r"c:\user\pwd\"
  File "<stdin>", line 1
    chai = r"c:\user\pwd\"
           ^
SyntaxError: unterminated string literal (detected at line 1); perhaps you escaped the end quote?
- >>> chai = r"c:\\user\pwd\\" 
- >>> print(chai)
c:\\user\pwd\\
- >>> chai = r"c:\user\pwd"    
- >>> print(chai)
c:\user\pwd
- >>> chai = "c:\user\pwd"  
  File "<stdin>", line 1
    chai = "c:\user\pwd"
           ^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
- >>> chai = "c:\\user\\pwd" 
- >>> chai 
'c:\\user\\pwd'
- >>> print(chai)
c:\user\pwd
- >>> chai = "Masala chai "
- >>> chai = "Masala chai"  
- >>> print("Masala" in chai )
True
- >>> print("Masalaa" in chai ) 
False
- >>> print("masala" in chai )  
False
- >>> print("Chai" in chai )
True

# list In Python 
# List :- Lists are ordered, mutable, and allow duplicate elements. They are defined using square brackets [].

# Example:
- >>> tea_varaities = ["Black", "Green","oolong","White"]
- >>> tea_varaities
['Black', 'Green', 'oolong', 'White']
- >>> print(tea_varaities)
['Black', 'Green', 'oolong', 'White']
- >>> print(tea_varaities[0]) 
Black
- >>> print(tea_varaities[1]) 
Green
- >>> print(tea_varaities[-1]) 
White
- >>> print(len(tea_varaities))    
4
- >>> print(tea_varaities[:2])  
['Black', 'Green']
- >>> print(tea_varaities[2:4]) 
['oolong', 'White']
- >>> print(tea_varaities[2:])  
['oolong', 'White']
- >>> tea_varaities[3]
'White'
- >>> tea_varaities[3] = "Herbal"
- >>> print(tea_varaities)     
['Black', 'Green', 'oolong', 'Herbal']
- >>> tea_varaities[1:2] 
['Green']
- >>> tea_varaities[1:2] = "lemon"
- >>> print(tea_varaities)
['Black', 'l', 'e', 'm', 'o', 'n', 'oolong', 'Herbal']
- >>> tea_varaities = ["Black", "Green","oolong","White"]
- >>> tea_varaities        
['Black', 'Green', 'oolong', 'White']
- >>> tea_varaities[1:2]          
['Green']
- >>> tea_varaities[1:2] = ['Lemon"]
  File "<stdin>", line 1
    tea_varaities[1:2] = ['Lemon"]
                          ^
SyntaxError: unterminated string literal (detected at line 1)
- >>> tea_varaities[1:2] = ["Lemon"] 
- >>> tea_varaities       
['Black', 'Lemon', 'oolong', 'White']
- >>> tea_varaities[1:3] 
['Lemon', 'oolong']
- >>> tea_varaities[1:3] = ["Green","Masala"]
- >>> tea_varaities      
['Black', 'Green', 'Masala', 'White']
- >>> tea_varaities[1:1]                     
[]
- >>> tea_varaities[1:1] = ["test", "test"] 
- >>> tea_varaities     
['Black', 'test', 'test', 'Green', 'Masala', 'White']
- >>> tea_varaities[1:2] 
['test']
- >>> tea_varaities[1:3] 
['test', 'test']
- >>> tea_varaities[1:3] = []
- >>> tea_varaities           
['Black', 'Green', 'Masala', 'White']
- >>> for tea in tea_varaities:
...     print(tea)
... 
Black
Green
Masala
White
- >>> for tea in tea_varaities:
...     print(tea, end="-")
... 
Black-Green-Masala-White->>> 
- >>> tea_varaities
['Black', 'Green', 'Masala', 'White']
- >>> if "Oolong" in tea_varaites:
...     print("I have Oolong tea")
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    if "Oolong" in tea_varaites:
                   ^^^^^^^^^^^^
NameError: name 'tea_varaites' is not defined. Did you mean: 'tea_varaities'?
- >>> if "Oolong" in tea_varaties: )
...     print("I have Oolong tea")
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    if "Oolong" in tea_varaties:
                   ^^^^^^^^^^^^
NameError: name 'tea_varaties' is not defined. Did you mean: 'tea_varaities'?
- >>> tea_varaites
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    tea_varaites
NameError: name 'tea_varaites' is not defined. Did you mean: 'tea_varaities'?
- >>> tea_varaites
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    tea_varaites
NameError: name 'tea_varaites' is not defined. Did you mean: 'tea_varaities'?
- >>> tea_varaities
['Black', 'Green', 'Masala', 'White']
- >>> if "Oolong" in tea_varaities:
...     print("I have Oolong tea")
... 
- >>> tea_varaities.append("Oolong")
- >>> tea_varaities
['Black', 'Green', 'Masala', 'White', 'Oolong']
- >>> tea_varaities.append("Oolong")
- >>>     print("I have Oolong tea") 
  File "<stdin>", line 1
        print("I have Oolong tea")
    ^
IndentationError: unexpected indent
- >>> tea_varaities
['Black', 'Green', 'Masala', 'White', 'Oolong', 'Oolong']
- >>> if "Oolong" in tea_varaities:) 
...     print("I have Oolong tea")
... 
I have Oolong tea
- >>> tea_varaities.pop()
'Oolong'
- >>> tea_varaities      
['Black', 'Green', 'Masala', 'White', 'Oolong']
- >>> tea_varaities.pop()
'Oolong'
- >>> tea_varaities      
['Black', 'Green', 'Masala', 'White']
- >>> tea_varaities.remove("Green")
- >>> tea_varaities
['Black', 'Masala', 'White']
- >>> tea_varaities.insert(1, "green") 
- >>> tea_varaities
['Black', 'green', 'Masala', 'White']

- >>> tea_varaities = ['Black', 'green', 'Masala', 'White']
- >>> tea_varaities_copy = tea_varaities.copy()
- >>> tea_varaities.append("Ginger") 
- >>> tea_varaities
['Black', 'green', 'Masala', 'White', 'Ginger']
- >>> tea_varaities_copy
['Black', 'green', 'Masala', 'White']
- > tea_varaities_copy.append("Red")
- > tea_varaities_copy              
['Black', 'green', 'Masala', 'White', 'Red']
- > tea_varaities     
['Black', 'green', 'Masala', 'White', 'Ginger']
- > squared_nums
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    squared_nums
NameError: name 'squared_nums' is not defined
- > squared_nums = [x**2 for x in range(10)] 
- > range(10)
range(0, 10)
- > print(range(10))
range(0, 10)
- > y = range(10)
- > y
range(0, 10)
- > squared_nums = [x**2 for x in range(10)]
- > sqaured_nums
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    sqaured_nums
NameError: name 'sqaured_nums' is not defined. Did you mean: 'squared_nums'?
- > squared_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
- > cube_nums = [y***3 for y in range(5)]
  File "<stdin>", line 1
    cube_nums = [y***3 for y in range(5)]
                    ^
SyntaxError: invalid syntax
- > cube_nums = [y**3 for y in range(5)]  
- > cube_nums
[0, 1, 8, 27, 64]


# Dictionaries :- Dictionaries are unordered, mutable, and allow duplicate values but not duplicate keys. They are defined using curly braces {} with key-value pairs.  
# Example:
- >>> tea_prices = {"Black": 10, "Green": 15, "Oolong": 20}
- >>> tea_prices
{'Black': 10, 'Green': 15, 'Oolong': 20}    

- > chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
- > chai_types["Masala"] 
'Spicy'
- > chai_types.get("Ginger")
'Zesty'
- > chai_types.get("Gingery\")
  File "<stdin>", line 1
    chai_types.get("Gingery\")
                   ^
SyntaxError: unterminated string literal (detected at line 1); perhaps you escaped the end quote?
- > chai_types.get("Gingery")  
- > chai_types["Masalaa"]      
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types["Masalaa"]
    ~~~~~~~~~~^^^^^^^^^^^
KeyError: 'Masalaa'
- > chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
- > chai_types["Green"] = "Fresh"
- > chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
- > for chai in chai_types:
...     print(chai)
... 
Masala
Ginger
Green
- > for chai in chai_types:
...     print(chai, chai_types[chai])
... 
Masala Spicy
Ginger Zesty
Green Fresh
- > for key, values in chai_types.items():
...     print(key,values)
... 
Masala Spicy
Ginger Zesty
Green Fresh
- > for key, value in chai_types.items():  
...     print(key,value)
... 
Masala Spicy
Ginger Zesty
Green Fresh
- > if"Masala" in chai_types: 
...     print("I have Masala chai")
... 
I have Masala chai
- >     print("I"))))))))))))))))))
  File "<stdin>", line 1
        print("I")
    ^
IndentationError: unexpected indent
- > print(len(chai_types)) 
3
- > chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
- > chai_types["Earl Grey"] = "Citrus"
- > chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
- > chai_types.pop("Ginger") 
'Zesty'
- > chai_types
{'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
- > chai_types.popitem()
('Earl Grey', 'Citrus')
- > chai_types
{'Masala': 'Spicy', 'Green': 'Fresh'}
- > del chai_types["Green"]
- > chai_types
{'Masala': 'Spicy'}
- > chai_types_copy = chai_types_copy()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types_copy = chai_types_copy()
                      ^^^^^^^^^^^^^^^
NameError: name 'chai_types_copy' is not defined
- > chai_types_copy = chai_types.copy()
- > tea_shop = {
...     "chai":{"Masala":"Spicy","Ginge":"Zesty"},
...     "Tea":{"Green":"Mild","Black":"Strong"}
... }
- > tea_shop
- > tea_shop
{'chai': {'Masala': 'Spicy', 'Ginge': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
- > print(tea_shop)
{'chai': {'Masala': 'Spicy', 'Ginge': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
{'chai': {'Masala': 'Spicy', 'Ginge': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
- > print(tea_shop)
{'chai': {'Masala': 'Spicy', 'Ginge': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
- > tea_shop['chai']
{'Masala': 'Spicy', 'Ginge': 'Zesty'}
- > tea_shop['chai']["Ginger"]
- > tea_shop['chai']
{'Masala': 'Spicy', 'Ginge': 'Zesty'}
- > tea_shop['chai']["Ginger"]
-raceback (most recent call last):
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    tea_shop['chai']["Ginger"]
  File "<stdin>", line 1, in <module>
    tea_shop['chai']["Ginger"]
    ~~~~~~~~~~~~~~~~^^^^^^^^^^
KeyError: 'Ginger'
    ~~~~~~~~~~~~~~~~^^^^^^^^^^
KeyError: 'Ginger'
- > tea_shop['chai']["Ginge"]
'Zesty'
- > squared_num = {x:x**2 for x in range(6)}
- > squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
- > squared_num.clear()
- > squared_num
{}
- > default_value = "Delicious"
- > new_dict = dict.fromkeys(keys, default_value)
- > new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
- > new_dict = dict.fromkeys(keys, keys)
- > new_dict
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}


# Tuples :- Tuples are ordered, immutable, and allow duplicate elements. They are defined using parentheses ().
# Example:
- >>> tea_tuple = ("Black", "Green", "Oolong", "White")
- >>> tea_tuple
('Black', 'Green', 'Oolong', 'White')
- >>> print(tea_tuple)
('Black', 'Green', 'Oolong', 'White')
- >>> print(tea_tuple[0])
Black
- >>> print(tea_tuple[1])
Green
- >>> print(tea_tuple[-1])
White
- >>> print(len(tea_tuple))
4
- >>> print(tea_tuple[:2])
('Black', 'Green')  
- >>> print(tea_tuple[2:4])
('Oolong', 'White')
- >>> print(tea_tuple[2:])
('Oolong', 'White')
- >>> tea_tuple[3]
'White'
- >>> tea_tuple[3] = "Herbal"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    tea_tuple[3] = "Herbal"
TypeError: 'tuple' object does not support item assignment
- >>> tea_tuple = ("Black", "Green", "Oolong", "White")
- >>> tea_tuple
('Black', 'Green', 'Oolong', 'White')

- >>> len(tea_tuple)
4

- > tea_types = ("Black","Green","Oolong")
- > tea_types
('Black', 'Green', 'Oolong')
- > print(tea_types)
('Black', 'Green', 'Oolong')
- > tea_types[0]     
'Black'
- > tea_types[-1] 
'Oolong'
- > tea_types[1:0] 
()  
- > tea_types[1:1] 
()
- > more_tea = ("Herbal","Earl Grey")
- > all_tea = more_tea + tea_types
- > all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
- > if "Green" in all_tea:
...     print("I have Green Tea")
... 
I have Green Tea
- > more_tea = ("Herbal", "Earl Grey", "Herbal")
- > more_tea
('Herbal', 'Earl Grey', 'Herbal')
- > more_tea.count("Herbal")
2
- > tea_types
('Black', 'Green', 'Oolong')
- > (black, green, Oolong) = tea_types
- > black
'Black'
- > Oolong
'Oolong'
- > green
'Green'
- > type(tea_types) 
<class 'tuple'>
- > ("",(1,2,3,4),"")
('', (1, 2, 3, 4), '')
