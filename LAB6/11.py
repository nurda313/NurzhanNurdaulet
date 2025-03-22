list = []
q = int(input("Enter the number of the list: "))
for i in range(q):
    items = int(input("Enter the number: "))
    list.append(items)


for num in list:
    mul = num * num

print(mul)