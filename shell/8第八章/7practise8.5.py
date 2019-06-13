def san(*material):
        print(material)

def build_profile(first_name,last_name,**info):
        result = {}
        result["first_name"]=first_name
        result["last_name"]=last_name
        for key,value in info.items():
                result[key]=value
        return result

def user_profile():
        users=[]
        while True:
                info={}
                first_name=input("first_name:")
                if first_name == 'q':
                   break     
                last_name=input("last_name:")
                info["age"]=input("age:")
                info["weight"]=input("weight:")
                users.append(build_profile(first_name,last_name,age=info["age"],weight=info["weight"]))
        print(users)

san("芝麻","香蕉","奶油")
san("1","2","3")
san("成功","失败")

user_profile()