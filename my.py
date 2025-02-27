num1 = int(input())
num2 = int(input())
char = str(input())
if char == "+":
    sum = num1 + num2
    print(num1, num2, sep = "+", end = f"={sum}\n")
    

elif char == "-":
    sum = num1 - num2
    print(num1, num2, sep = "-", end = f"={sum}\n")
    

elif char == "*":
    sum = num1 * num2
    print(num1, num2, sep = "*", end = f"={sum}\n")
    

elif char == "/":
    sum = num1 / num2
    print(num1, num2, sep = "/", end = f"={sum}\n")
    