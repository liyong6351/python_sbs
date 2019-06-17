while True:
    try:
        num1=input("please input the first number:")
        if num1 == 'q':
            break
        num2=input("please input the second number:")
        print("add result=" + str(int(num1) + int(num2)))
    except ValueError as ve:
        print(str(ve))
    else:
        print("Greate")
    finally:
        print("finally")

print("here is the dog information for u:")
try:
    with open("data/dog.txt") as dog:
        dogs=dog.read()
except FileNotFoundError as fn:
    print(str(fn) + " 文件去月球了，您要等等哈")    
else:
    print(dogs)

print("here is the cat information for u:")
try:
    with open("data/cat1.txt") as cat:
        cats=cat.read()
except FileNotFoundError as fn:
    print(str(fn) + " 文件去月球了，您要等等哈")    
else:
    print(cats)