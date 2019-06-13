message = input("please input the message:")
print("message=" + message)

age=input("please input your age:")
if int(age) > 18:
    print("你已成年！")
else:
    print("你还小着呢!")

if int(age) % 3 == 0:
    print(age + " 是2的倍数!")
else:
    print(age + " 不是2的倍数")