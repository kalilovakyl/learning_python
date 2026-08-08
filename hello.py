print("Hello");
# This is comment
'''
This is also comment
'''

# Integer 
a = 5

# Floating-point 
b = 1.2

'''
String
'''
c = "String"

print(f"Integer: {a},\nFloating-point: {b},\nString: {c}")
'''
This print message looks weird in syntax but works)
'''

# All data types in one variable

x = "Hello" # This is string number
x = 50 
""" 
Above is integer
"""
x = 4.5 # This is floating-point number
x = 5j # This is complex number
x = ["one", "two", "three"] # This is list
x = ("one", "three", "two") # This is tuple
x = {"name": "Akyl", "age": 20} # This is dictionary
x = {"what", "is", "set"} # This is set
x = True # This is boolean
x = b"geeks" # This is binary not really know what it means

print(x) # Must print binary number

name = input("Enter your name: ")
age = float(input("Enter your age: "))
print(f"Hello {name}, you are {age} old")
print(type(name))
print(type(age))
