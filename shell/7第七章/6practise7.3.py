active=True
while active:
    message=input("please input the name:")
    if message == 'q':
        active=False
    else:
        print("you input the name:" + message)

active=True
while active:
    age=input("please input the age:")
    if age == 'q':
        active=False
    elif int(age)<3:
        print("免费")
    elif int(age) <= 12:
        print("票价10元")
    else:
        print("票价15元")