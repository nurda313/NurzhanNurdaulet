import os

path = input("Enter the path: ")

if os.path.exists(path):
    print("Directory:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\n Files:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

    print("\n📁 All content:")
    for item in os.listdir(path):
        print(item)
else:
    print("Not found.")
