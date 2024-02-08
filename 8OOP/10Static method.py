class Student:
    # class_Variable
    category="Student"
    
    def __init__(self,name):
        #instance variable
        
        self.name =name
    
    #instance method: is a method that access instance variable
    def hello(self):
        print(f"Hello my name is {self.name}")
        
    #instance method
    
    def length(self):
        
        return len(self.name)
    # class method dont use self uses cls
    @classmethod
    def info (cls):
        print(f"this is a method of the class {cls.category}")
    
    @staticmethod
    #static method dont use self or cls instead uses decorator
    def add(a,b):
        print(a+b)
        
# ex 
class Circle:
    
    @staticmethod
    def area(r):
        return 3.14*r*r
    
    @staticmethod
    def circumference(r):
        return 2*3.14*r
      

Student.add(2,3)
a=Circle.area(10)
print(a)
c=Circle.circumference(10)
print(c)