car=input("please input the car brand:")
print("let me find out the " + car.title())

num = input("please input how many people u followed:")
if int(num) > 8:
    print("人太多了，没桌子!")
else:
    print("快来吧，来晚了就没桌子啦~")

num = input("请输入一个整数:")
if int(num) % 10 == 0:
    print("是10的整数倍")
else:
    print("不是10的整数倍")