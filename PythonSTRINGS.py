#Python Strings

print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


a = "Hello"
print(a)

#Slicing Strings

b = "Hello, World!"
print(b[2:])

print(b[:2])

print(b[::2])

#Modify Strings

a = "Hello, World!" #lower
print(a.lower())

a = "Hello, World!" #upper
print(a.upper())

a = " Hello, World! " #strip/delete extra elements from the sides
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!" #replace
print(a.replace("H", "J"))

a = "Hello, World!" #split
print(a.split(",")) 

#String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello" #to add space
b = "World"
c = a + " " + b
print(c)