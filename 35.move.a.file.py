import os

source = "test35.txt"
destination = "D:\\study\\python\\py_tutorial\\folder\\test35.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")

