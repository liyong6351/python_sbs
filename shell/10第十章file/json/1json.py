import json

numbers=[1,2,3,4,5,6,7,8]
number1=[]
try:
    with open("data/json.txt","w") as js:
        json.dump(numbers,js)
except FileNotFoundError as fn:
    print(str(fn))    
else:
    print("Greate !")

print(number1)
try:
    with open("data/json.txt") as js:
        number1 = json.load(js)
except FileNotFoundError as fn:
    print(str(fn))    
else:
    print("Greate !")
print(number1)