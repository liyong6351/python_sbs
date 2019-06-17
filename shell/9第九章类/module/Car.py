# 一个表示汽车的类

class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    
    def get_desc_name(self):
        return str(self.year) + " " + str(self.make) + " " + str(self.model)
        
    def reading_odometer(self):
        return str(self.odometer_reading) + "miles"
        
    def update_odometer(self):
        return "Car Car Car"

class Electric_Car(Car):
    def __init__(self,make,model,year,oil)
    super().__init__(make,model,year)
    self.oil="no need oil,use electric"

    def get_desc_name(self):
        return super().get_desc_name() + " child=elec"