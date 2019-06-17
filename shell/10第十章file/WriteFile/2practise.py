with open("data/practise.txt","a") as guest:
    while True:
        name=input("please input your name:")
        if(name == 'q'):
            break
        else:
            guest.write("name=" + name +"\n")