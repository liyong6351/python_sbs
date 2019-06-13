def format(first_name="default first_name",last_name="default_last_name"):
    full_name = (first_name + " " + last_name)
    return full_name.title()

def returnDic(first_name="default first_name",last_name="default_last_name"):
    result={}
    result["first_name"]=first_name
    result["last_name"]=last_name
    result["full_name"]=format(first_name,last_name)
    return result

print(format())
print(format("li","lei"))

print(returnDic())
print(returnDic("li","lei"))
