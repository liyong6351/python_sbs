class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    
    def get_desc_name(self):
        long_name=str(self.year) + " " + str(self.make) + " " + str(self.model)
        print(long_name)
        return long_name

    def reading_odometer(self):
        print(str(self.odometer_reading) + "miles")
    
    def update_odometer(self):
        print("Car Car Car")

class ElectricCar(Car):
    def __init__(self,oil,make="maker",model="model",year=1985):
        super().__init__(make,model,year)
        self.oil=oil

    def find(self):
        print("find " + self.make)

    def getOil(self):
        print("oil= " + self.oil)
    
    def get_desc_name(self):
        long_name=str(super().get_desc_name()) + " oil=" + self.oil
        print(long_name)
    
c = ElectricCar(oil="gasline")
c.update_odometer()
c.find()
c.getOil()
c.get_desc_name()