
class Dog:
    """ 
    Attempt to make a dog
    This Class has various methods to call.
    """

    #__init__ method gets called every time a class is instantiaed, usually used to instantiate attributes. Every method should have self parameter called to grab instance.
    def __init__(self, name, age):
        """Initializes name and age attributes"""
        self.name = name
        self.age = age
        self.distance_run = 0
    
    
    #Methods for class
    def sit(self):
        """Simulate dog sitting after commanded"""
        print(f"{self.name} is now sitting")
    
    def roll_over(self):
        """Simulate rolling over after commanded"""
        print(f"{self.name} just rolled over")
    
    def run_distance(self, distance):
        """Simulate dog running for some distance"""
        self.distance_run += distance
        print(f"{self.name} has run {self.distance_run} miles")

#instantiate class, look at init method to see parameters needed 
my_dog = Dog("Howie", 2)

#call class attributes
print(f"my dogs name is {my_dog.name}")
print(f"my dogs age is {my_dog.age}")

#call class methods
my_dog.sit()
my_dog.roll_over()
my_dog.run_distance(0)
my_dog.run_distance(5)
my_dog.run_distance(5)
