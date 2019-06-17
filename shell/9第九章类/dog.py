class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print("dog " + self.name + " has siting down")
    def roll_over(self):
        print("dog " + self.name + " is rolling_over")
    def desc(self):
        print("name=" + self.name + " age=" + str(self.age))

def descDog(dog):
    dog.desc()
    dog.sit()
    dog.roll_over()

my_dog=Dog("willie",6)
your_dog=Dog("wanner",8)
descDog(my_dog)
descDog(your_dog)
