current_number=1
while current_number < 10:
    print(current_number)
    current_number += 1

message=""
while message != 'q':
    message = input("please input the message:")
    print("you input :" + message)

active=True
while active:
    message=input("please input the message:")
    if message == 'q':
        active=False
    else:
        print("you input :" + message)