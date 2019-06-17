class Restaurant():
    def __init__(self,name,location):
        self.name=name
        self.location=location
    
    def desc(self):
        full_msg= "name="+self.name + " location="+self.location
        print(full_msg)
        return full_msg
    
    def open(self):
        print("restaurant " + self.name + " is open")

class IceCreamStand(Restaurant):
    def __init__(self,name,location,flavors):
        super().__init__(name,location)
        self.flavors=flavors
    
    def desc(self):
        return super().desc() + " flavors=" + str(self.flavors)

ice = IceCreamStand("ice","在这里",["你好","shijie"])
print(ice.desc())