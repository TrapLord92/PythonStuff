#creatingclass
class Vehicle:
    #creating_class attribute
    class_attribute="this is a vehicle class"
    
    # creating a class method
    @classmethod
    def class_method(cls):
        print(f"This is a class method , and i have acess to the the class atribute{cls.class_attribute}")
    #creating static method
    @staticmethod
    def static_method():
        print("Iam static method")
    
    #creating a constructor
    def __init__(self,name,color):
        #instance variables
        self.name=name
        self.color=color
    #instance method because uses instance variables
    def display_info(self):
        print(f"The {self.name} with beautiful {self.color} color")
        
        
#class inheritance  
class Car(Vehicle):
    #constructor overriding
    def __init__(self,name,color,fuel_type):
        super().__init__(name,color)
        self.fuel_type=fuel_type
    #method overriding
    def display_info(self):
        print(f"Name: {self.name}, Color:{self.color},fuel type : {self.fuel_type}")
        
#Create an object

vehicle=Vehicle("Cool car","red")
vehicle.display_info()
vehicle.class_method()
vehicle.static_method()

car =Car("Luxury car","Black","Diesel")
car.display_info()


        
        