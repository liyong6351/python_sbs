print("----first time----")
with open("data/learning_python.txt") as file_object:
    print(file_object.read())

print("----second time----")
with open("data/learning_python.txt") as file_object:
    for content in file_object.readlines():
        print(content.strip())

print("----third time----")
lines=[]
with open("data/learning_python.txt") as file_object:
    lines = file_object.readlines()

for content in lines:
    print(content.strip())

print("----fourth time----")
for content in lines:
    print(content.strip().replace("if","elif"))