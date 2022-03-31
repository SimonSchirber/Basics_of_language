#inheritance can take attributes of a class an make it into sub-class

#general classs of cars gasoline and electric cars can inherherit from
class Car:
    """Simple attempt to make a car"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    #methods
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

#inherited class from Car, add more features specific to electric cars
class ElectricCar(Car):
    """Represents aspects of a car, specific to Electric vehicles"""

    def __init__(self, make, model, year):
        """Initializes attributes of parent class"""
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def describe_battery(self):
        """Print statement describing battery"""
        print(f"This car has {self.battery_size} battery left")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()