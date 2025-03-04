
class Car:
    def __init__(self, brand, color):
        self.brand = brand  
        self.color = color  

    def start(self):
        print(f"The {self.color} {self.brand} car is starting.")


my_car = Car("Kia", "blue")
my_car.start() 
