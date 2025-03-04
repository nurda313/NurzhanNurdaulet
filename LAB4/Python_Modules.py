#Save this code in a file named mymodule.py

def greeting(name):
  print("Hello, " + name)


#Import the module named mymodule, and call the greeting function:

import mymodule

mymodule.greeting("Jonathan")


#Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}


#Import the module named mymodule, and access the person1 dictionary:

import mymodule

a = mymodule.person1["age"]
print(a)


#Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)


#Import and use the platform module:

import platform

x = platform.system()
print(x)


#There is a built-in function to list all 
#the function names (or variable names) in a module. The dir() function:

import platform

x = dir(platform)
print(x)


#The module named mymodule has one function and one dictionary:

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}


#Import only the person1 dictionary from the module:
from mymodule import person1

print (person1["age"])

