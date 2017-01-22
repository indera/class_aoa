
import dis

def swap1():
    a = 5
    b = 4
    a, b = b, a

def swap2():
    a = 5
    b = 4
    c = a
    a = b
    b = c

print('swap1():')
dis.dis(swap1)

print('swap2():')
dis.dis(swap2)

"""
ROT_TWO - Swaps the two top-most stack items.

swap1():
  5           0 LOAD_CONST               1 (5)
              3 STORE_FAST               0 (a)

  6           6 LOAD_CONST               2 (4)
              9 STORE_FAST               1 (b)

  7          12 LOAD_FAST                1 (b)
             15 LOAD_FAST                0 (a)
             18 ROT_TWO
             19 STORE_FAST               0 (a)
             22 STORE_FAST               1 (b)
             25 LOAD_CONST               0 (None)
             28 RETURN_VALUE
swap2():
 10           0 LOAD_CONST               1 (5)
              3 STORE_FAST               0 (a)

 11           6 LOAD_CONST               2 (4)
              9 STORE_FAST               1 (b)

 12          12 LOAD_FAST                0 (a)
             15 STORE_FAST               2 (c)

 13          18 LOAD_FAST                1 (b)
             21 STORE_FAST               0 (a)

 14          24 LOAD_FAST                2 (c)
             27 STORE_FAST               1 (b)
             30 LOAD_CONST               0 (None)
             33 RETURN_VALUE
"""
