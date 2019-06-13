cars=["audi","bmW","subaru","toyota"]
for car in cars:
    if car.lower() == "bmw":
        print(car.upper())
    else:
        if car != "audi":
            print(car.title())
        else: 
            print(car.lower())

print("---------数组-------------")
nums=[]
nums=[value**3 for value in range(1,20)]
print(nums)
for num in nums:
    if num<100:
        print(str(num) + " little than 100")
    elif num<1000:
        print(str(num) + " little than 1000")
    elif num < 10000:
        print(str(num) + " little than 10000")

for num in nums:
    if num > 5000 or num < 200:
        print(str(num) + " larger than 500 or little than 200")
    elif num > 300 and num < 450:
        print(str(num) + " larger than 300 or little than 450")
    else:
        print(str(num) + " other wise")

print(6859 in nums)

print(233 not in nums)

print("-------练习 5-3---------")
color="red"
if color == "green":
    print("u get 5 point!")
elif color == "yellow":
    print("u get 10 point!")
elif color == "red":
    print("u get 15 point!")

temp=[]
if temp:
    print("temp is not null ")
else:
    print(temp)

print("-------练习 5-4---------")

users=["lily","lucy","hanmeimei","lilei","jim","admin"]
#users=[]
if users:
    for u in users:
        print("Hello ",end=u)
        if u == "admin":
            print(", would u like look at the report!")
        else:
            print(", thank you to login in again!")
else:
    print("u need to find someone!")

current_users=users[:]
new_users=["guojin","yangguo","lilei","huyidao","qiaofeng"]
for u in new_users:
    if u in current_users:
        print("username used,please chose another one")
    else:
        print("username valid")

nums=[value for value in range(1,10)]
print(nums)
for num in nums:
    print(num,end="")
    if num == 1:
        print("st")
    elif num == 2:
        print("nd")
    elif num == 3:
        print("rd")
    else:
        print("th")