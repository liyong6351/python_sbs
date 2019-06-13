citys=["1重庆","2成都","3西安","4兰州"]
for city in citys:
    print("---------------")
    print("welcome to " + city)
    print("I wanner back to u " + city)
print("everybody goodnight!".title())

print("--------------pizza----------------")
pizzas=["sichuan","shanxi","beijing","guangdong"]
for pizza in pizzas:
    print("I like " + pizza + " pizza")
print("I like pizza very much!!!")

print("--------------animal---------------")
animals=["dog","cat","horse","duck"]
for animal in animals:
    print("A " + animal + " would make a great pet!")
print("Any of these animals would make a great pet!!!")

print("------------number arrays-------------")
for value in range(1,5):
    print("make a number " + str(value))

print("------将range转换为list--------")
nums = list(range(0,10))
for num in nums:
    print(num)

print("-------range定步长--------")
nums = list(range(0,50,3))
for num in nums:
    print(num)

print("-----------乘方运算------------")
pows=[]
for num in range(0,10):
    pows.append(num**3)
for num in pows:
    print(num)
print(min(pows))
print(max(pows))
print(sum(pows))

print("-----------列表解析----------")
squares=[value+100 for value in range(1,10)]
print(squares)

print("----------4.3练习题-------------")
p1 = []
p1 = [value for value in range(1,21)]
print(p1)
p1 = [value for value in range(1,11)]
for num in p1:
    print(num)
print(sum(p1))
p1 = [value for value in range(1,101,2)]
print(p1)
p1 = [value for value in range(3,31,3)]
print(p1)
p1 = [value**3 for value in range(1,11)]
print(p1)
print("------切片-----------")
p1 = [value**3 for value in range(1,11)]
print(p1[0:3])
print(p1[3:6])
print(p1[:6])
print(p1[0:100])
print(p1[-3:100])

for num in p1[-5:]:
    print(num)

print("------复制-----")
citys=["重庆","成都","北京","上海"]
print(citys)
citys1=citys[:]
print(citys1)
citys2=citys[-2:]
print(citys2)
citys1[0]="天津"
print(citys)
print(citys1)
# citys1=citys这样的拷贝表示仅仅拷贝了引用，而citys1=citys[:]表示深拷贝，同时拷贝了副本

print("-------练习4.4------")
citys=["重庆","成都","北京","上海","天津","广州","深圳","延吉"]
print("The first three city is  " + str(citys[:3]))
print("The last three city is  " + str(citys[-3:]))
print("The middle three city is  " + str(citys[3:6]))

your_citys=citys[:]
my_citys=citys[:]
your_citys.append("兰州")
my_citys.append("荣昌")
print(your_citys)
print(my_citys)
citys=[["密云","海淀","房山"],["荣昌","沙坪坝","九龙坡","渝北"],["徐汇","松江","奉贤"]]
for big in citys:
    print(big)
    for small in big:
        print(small)

print("--------元组-----------")
# 元组和列表是一样的，只是使用()看来标识,元组的元素不能修改但可以重新定义
demensions=(200,50)
print(demensions)
print(demensions[0])
for num in demensions:
    print(num)
demensions=(100,20)
for num in demensions:
    print(num)

print("-----------4.5练习---------")
foods=["bread","pizza","chinese food","cake","choclate"]
for food in foods:
    print(food)
foods=["bread","pizza","chinese food","cake1","choclate1"]
for food in foods:
    print(food)