class Restaurant():
    def __init__(self,name,location):
        self.name=name
        self.location=location
    
    def desc(self):
        print("name="+self.name + " location="+self.location)
    
    def open(self):
        print("restaurant " + self.name + " is open")

class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    
    def desc(self):
        print("first_name="+self.first_name + " last_name="+self.last_name)

    def greet(self):
        print("hello,I am " + self.first_name)

my_res=Restaurant("西点餐厅","振宁路")
your_res=Restaurant("懂点餐厅","盈丰路")

print(my_res.name + " " + my_res.location)
print(your_res.name + " " + your_res.location)

lily=User("lily","join")
lily.desc()
lily.greet()
lily.first_name="changed"
lily.desc()