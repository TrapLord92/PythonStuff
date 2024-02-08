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

student=Student("Jaime")
Student.info()#class accessing class method
 
print(student.hello())
length=student.length()
print(student.info())

print(length)
 