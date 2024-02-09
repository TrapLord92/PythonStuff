class Car:
    def __init__(self,brand):
        self.brand=brand
        self.steering_object=self.Steering()
    
    @staticmethod
    def drive():
        print("Drive")
        
    
    class Steering:
        @staticmethod
        def rotate():
            print("rotate")
            
            
car=Car("Toyota")
print(car.brand)
car.drive()

steering=car.Steering
steering.rotate()