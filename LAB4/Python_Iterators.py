#1  Generator that generates squares up to N

def square_gen(n):
    for i in range(n + 1):
        yield i * i

for num in square_gen(10):
    print(num, end=" ")



#2  Generator for even numbers up to n
def even_gen(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())
print(",".join(map(str, even_gen(n))))

  


#3 Generator for numbers divisible by 3 and 4
def div_gen(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in div_gen(50):
    print(num, end=" ")




#4 Generator squares(a, b) to yield squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for num in squares(3, 7):
    print(num)




#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num, end=" ")
