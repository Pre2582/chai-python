# Example of Iteration Tools in Python

>>> open('chai.py') 
<_io.TextIOWrapper name='chai.py' mode='r' encoding='cp1252'>
>>> f = open('chai.py')
>>> f.readline()        
'# Iteration tools\n'
>>> f.readline()
'# https://docs.python.org/3/library/itertools.html\n'
>>> f = open('chai.py')
>>> f.readline()        
'\n'
>>> f.readline()        
'import time \n'
>>> f.readline()        
'print("Chai is  here")\n'
>>> f = open('chai.py')
>>> f.__next__()
'\n'
>>> f.__next__()
'import time \n'
>>> f.__next__()
'print("Chai is  here")\n'
>>> f.__next__()
"username = 'prem'\n"
>>> f.__next__()
'print("Welcome", username)\n'
>>> f.__next__()
'\n'
>>> f.__next__()
'# Iteration tools\n'
>>> f.__next__()
'# https://docs.python.org/3/library/itertools.html\n'
>>> f.__next__()
'# import itertools\n'
>>> f.__next__()
'# # Infinite counting\n'
>>> f.__next__()
'# for i in itertools.count(10, 2):\n'
>>> f.__next__()
'#     print(i)\n'
>>> f.__next__()
'#     if i >= 20:\n'
>>> f.__next__()
'#         break   \n'
>>> f.__next__()
'\n'
>>> f.__next__()
'# Iteration tool to repeat an action a certain number of times  (For, comprehension, while)\n'
>>> f.__next__()
'# Iterable objects (list, tuple, set, dict, string, file) \n'
>>> f.__next__()
'# __next__() method to get the next item from the iterator\n'
>>> f.__next__()
'# StopIteration exception to signal the end of the iteration`\n'
>>> for line in open('chai.py'):     
...     print(line)
... 


import time

print("Chai is  here")

username = 'prem'

print("Welcome", username)



- >> Iteration tools

 https://docs.python.org/3/library/itertools.html
 import itertools
 # Infinite counting
 for i in itertools.count(10, 2):
     print(i)
     if i >= 20:
         break

 Iteration tool to repeat an action a certain number of times  (For, comprehension, while)
 Iterable objects (list, tuple, set, dict, string, file)
 __next__() method to get the next item from the iterator
 StopIteration exception to signal the end of the iteration`

- >>     print(line, end='')
  File "<stdin>", line 1
        print(line, end='')
    ^
IndentationError: unexpected indent
- >>> for line in open('chai.py'):
...     print(line, end="")
... 

import time
print("Chai is  here")
username = 'prem'
print("Welcome", username)



- >> Iteration tools

 https://docs.python.org/3/library/itertools.html
 import itertools
 # Infinite counting
 for i in itertools.count(10, 2):
     print(i)
     if i >= 20:
         break
 Iteration tool to repeat an action a certain number of times  (For, comprehension, while)
 Iterable objects (list, tuple, set, dict, string, file)
 __next__() method to get the next item from the iterator
 StopIteration exception to signal the end of the iteration`
- >>> f = open('chai.py')
- >>> while True:
...     line = f.readline()
...     if not line: break
...     print(line, end='')
... 

import time
print("Chai is  here")
username = 'prem'
print("Welcome", username)

- Iteration tools
- https://docs.python.org/3/library/itertools.html
- import itertools
- # Infinite counting
- for i in itertools.count(10, 2):
-     print(i)
-     if i >= 20:
-         brea- 
- Iteration tool to repeat an action a certain number of times  (For, comprehension, while)
- Iterable objects (list, tuple, set, dict, string, file)
- __next__() method to get the next item from the iterator
- StopIteration exception to signal the end of the iteration`
- >>> test = "hitesh"
- >>> if not test:
...     print("chai")
...  
- >>> test = ""
- >>> if not test:
...     print("Chai")
... 
Chai
- >>> myList = [1,2,3,4]
- >>> I = iter(myList)
- >>> I
<list_iterator object at 0x000001B4A0F39F00>
- >>> I.__next__()
1
- >>> I
<list_iterator object at 0x000001B4A0F39F00>
- >>> I.__next__()
2
- >>> I.__next__()
3
- >>> I.__next__()
4
- >>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    I.__next__()
    ~~~~~~~~~~^^
StopIteration
- >>> f = open('chai.py')
- >>> iter(f) is f
True
- >>> iter(f) is f.__iter__()
True
- >>> myNewList = [1,2,3]
- >>> iter(myNewList)
<list_iterator object at 0x000001B4A0F86350>
- >>> iter(myNewList) is myNewList
False
- >>> D = {'a': 1,'b':2}
- >>> for key in D.keys():
...     print(key)
... 
a
b
- >>> I = iter(D)
- >>> I
<dict_keyiterator object at 0x000001B4A10181D0>
- >>> next(I) 
'a'
- >>> next(I)
'b'
- >>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration
- >>> range(5)
range(0, 5)
- >>> R = range(5)
- >>> R
range(0, 5)
- >>> I =iter(R)
- >>> next(I)
0
- >>> next(I)
1
- >>> next(I)
2
- >>> next(I)
3
- >>> next(I)
4
- >>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration