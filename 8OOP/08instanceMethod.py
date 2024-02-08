class Student:
    def __init__(self,name):
        #instance variable
        
        self.name =name
    
    #instance method: is a method that access instance variable
    def hello(self):
        print(f"Hello my name is {self.name}")
        
    #instance method
    
    def length(self):
        
        return len(self.name)


student=Student("Jaime")
 
print(student.hello())
length=student.length()

print(length)
 