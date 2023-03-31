# This is a Python program that covers all the basic syntax

# Output a string to the console
# The print() function is used to output a string to the console
print("Hello World")

# Variable declaration and initialization
x = 3
y = 4.5
z = "Hello World"

# Data types
print(type(x)) # int
print(type(y)) # float
print(type(z)) # str

# Arithmetic operations

a = x + y # Addition
b = x - y # Subtraction
c = x * y # Multiplication
d = x / y # Division
e = x % y # Modulus
f = x ** y # Exponentiation

print(a) # 7.5
print(b) # -1.5
print(c) # 13.5
print(d) # 0.6666666666666666
print(e) # 3.0
print(f) # 81.0701484375

# Comparison operators
print(x == y) # False
print(x != y) # True
print(x > y) # False
print(x < y) # True
print(x >= y) # False
print(x <= y) # True

# Logical operators
print(x == 3 and y == 4.5) # True
print(x == 3 or y == 4.5) # True    
print(not(x == 3 and y == 4.5)) # False

p = True    # True
q = False   # False
print(p and q) # False
print(p or q) # True
print(not p) # False

# Conditional statements
if x == 3:
    print("x is equal to 3")    # x is equal to 3
elif x == 4:
    print("x is equal to 4")    # x is equal to 4
else:
    print("x is not equal to 3 or 4")   # x is not equal to 3 or 4

# Loops
# For loop
for i in range(0, 10): 
    print(i)    # 0 1 2 3 4 5 6 7 8 9

# While loop
i = 0
while i < 10:
    print(i)    # 0 1 2 3 4 5 6 7 8 9
    i += 1

# Functions

def add(x, y):
    return x + y

print(add(3, 4)) # 7    

# lists
list1 = [1, 2, 3, 4, 5]
print(list1[0]) # 1
print(list1[1]) # 2
print(list1[2]) # 3
print(list1[3]) # 4
print(list1[4]) # 5
print(list1[1:4]) # [2, 3, 4]

list1[1] = list1[1] + 1
print(list1[1]) # 3
list1[1] += list1[1] # list1[1] = list1[1] + list1[1]
print(list1[1]) # 6


# dictionaries
dict1 = {"name":"xixi", "age":1.5, "father":"liuyi", "mother":"jj"}
print(dict1) # {'name': 'xixi', 'age': 1.5, 'father': 'liuyi', 'mother': 'jj'}
print(dict1["name"]) # xixi
print(dict1["age"]) # 1.5
print(dict1["father"]) # liuyi
print(dict1["mother"]) # jj

# tuples
tuple1 = (1, 2, 3, 4, 5)
print(tuple1) # (1, 2, 3, 4, 5)
print(tuple1[0]) # 1
print(tuple1[1]) # 2
print(tuple1[2]) # 3
print(tuple1[3]) # 4
print(tuple1[4]) # 5
#tuple[1] = tuple[1] + 2 # TypeError: 'tuple' object does not support item assignment

# sets
set1 = {1, 2, 3, 4, 5}
print(set1) # {1, 2, 3, 4, 5}
set1.add(6)
print(set1) # {1, 2, 3, 4, 5, 6}
set1.remove(6)
print(set1) # {1, 2, 3, 4, 5}

# sets
set2 = {1.1, 2.2, 3.3, 4.4, 5.5}
set2.add(10)
print(set2) # {1.1, 2.2, 3.3, 4.4, 5.5, 10}
#set2.remove(1) # KeyError: 1
print(set2) # {2.2, 3.3, 4.4, 5.5, 10}

#set2(1) = set2(1) + 2 # TypeError: 'set' object does not support item assignment

set1.add(10)    # {1, 2, 3, 4, 5, 10}

set3 = set1 | set2 # {1, 2, 3, 4, 5, 10, 2.2, 3.3, 4.4, 5.5}
print(set3) # {1, 2, 3, 4, 5, 10, 2.2, 3.3, 4.4, 5.5}

set4 = set1 - set2 # {1, 2, 3, 4, 5}
set5 = set2 - set1 # {2.2, 3.3, 4.4, 5.5, 10}

set6 = set1 & set2 # {10}

set7 = set1 ^ set2 # {1, 2, 3, 4, 5, 2.2, 3.3, 4.4, 5.5}
print("Set7: ", set7) # Set7:  {1, 2, 3, 4, 5, 2.2, 3.3, 4.4, 5.5}
set8 = set7 & set6 
print("Set8: ", set8) # Set8:  set()


# list comprehension
list2 = [i for i in range(0, 10)]
print(list2) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list3 = [i for i in range(0, 10) if i % 2 == 0] 
print(list3) # [0, 2, 4, 6, 8]

list4 = [i for i in range(0, 10) if i % 2 == 0 if i % 3 == 0]
print(list4) # [0, 6]

list5 = [i if i % 2 == 0 else i * 2 for i in range(0, 10)]
print(list5) # [0, 2, 2, 6, 4, 10, 6, 14, 8, 18]

list6 = [i if i % 2==0 else i * 3 for i in range(10,20)]
print(list6) # [10, 33, 12, 39, 14, 45, 16, 51, 18, 57]

list7 = [i if i % 2==0 else i * 3 for i in range(10,20) if i % 3 == 0]
print(list7) # [12, 39, 18, 57]

list8 = [i if i % 2==0 else i * 3 for i in range(10,20) if i % 3 == 0 if i % 4 == 0]
print(list8) # [12, 57]

list9 = [i if i % 2==0 else i * 3 for i in range(10,20) if i % 3 == 0 if i % 4 == 0 if i % 5 == 0]
print(list9) # [12]


# dictionary comprehension
dict2 = {i: i * 2 for i in range(0, 10)}
print(dict2) # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}


# set comprehension
set9 = {i for i in range(0, 10)}
print(set9) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


# generator comprehension
gen1 = (i for i in range(0, 10))
print(gen1) # <generator object <genexpr> at 0x7f9b8c0b9f68>
print(next(gen1)) # 0
print(next(gen1)) # 1
print(next(gen1)) # 2
print(next(gen1)) # 3


# lambda function
def add(x, y):
    return x + y

print(add(1, 2)) # 3

add2 = lambda x, y: x + y
print(add2(1, 2)) # 3





