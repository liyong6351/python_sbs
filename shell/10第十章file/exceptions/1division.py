try:
    print(10/0)
except ZeroDivisionError as ze:
    print(str(ze))

try:
    with open("data/test_data.txt") as data:
        contents = data.read()
except FileNotFoundError as t:
    print("file not found")
else:
    words = split(" ")
    print(contents)
    print(len(words))