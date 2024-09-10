Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
a=np.arange(6).reshape(3,2)
b=np.arange(6,12).reshape(3,2)
a
array([[0, 1],
       [2, 3],
       [4, 5]])
b
array([[ 6,  7],
       [ 8,  9],
       [10, 11]])
np.vstack((a,b))
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11]])
np.hstack((a,b))
array([[ 0,  1,  6,  7],
       [ 2,  3,  8,  9],
       [ 4,  5, 10, 11]])




a=np.arange(30).reshape(2,15)
a
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])
np.hsplit(a,3)
[array([[ 0,  1,  2,  3,  4],
       [15, 16, 17, 18, 19]]), array([[ 5,  6,  7,  8,  9],
       [20, 21, 22, 23, 24]]), array([[10, 11, 12, 13, 14],
       [25, 26, 27, 28, 29]])]
result=np.hsplit(a,3)
result[0]
array([[ 0,  1,  2,  3,  4],
       [15, 16, 17, 18, 19]])
result[2]
array([[10, 11, 12, 13, 14],
       [25, 26, 27, 28, 29]])
np.vsplit(a,3)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    np.vsplit(a,3)
  File "C:\Users\yeamu\AppData\Roaming\Python\Python312\site-packages\numpy\lib\_shape_base_impl.py", line 1020, in vsplit
    return split(ary, indices_or_sections, 0)
  File "C:\Users\yeamu\AppData\Roaming\Python\Python312\site-packages\numpy\lib\_shape_base_impl.py", line 889, in split
    raise ValueError(
ValueError: array split does not result in an equal division
result=np.hsplit(a,2)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    result=np.hsplit(a,2)
  File "C:\Users\yeamu\AppData\Roaming\Python\Python312\site-packages\numpy\lib\_shape_base_impl.py", line 964, in hsplit
    return split(ary, indices_or_sections, 1)
  File "C:\Users\yeamu\AppData\Roaming\Python\Python312\site-packages\numpy\lib\_shape_base_impl.py", line 889, in split
    raise ValueError(
ValueError: array split does not result in an equal division
>>> result=result=np.vsplit(a,2)
>>> result[0]
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]])
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=np.arange(12).reshape(3,4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> b=a>4
>>> b
array([[False, False, False, False],
       [False,  True,  True,  True],
       [ True,  True,  True,  True]])
>>> [ True,  True,  True,  True]])a[b]
SyntaxError: unmatched ']'
>>> a[b]
array([ 5,  6,  7,  8,  9, 10, 11])
>>> a[b]=-a
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a[b]=-a
TypeError: NumPy boolean array indexing assignment requires a 0 or 1-dimensional input, input has 2 dimensions
>>> a[b]=-1
>>> a
array([[ 0,  1,  2,  3],
       [ 4, -1, -1, -1],
       [-1, -1, -1, -1]])
