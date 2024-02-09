class Student:
    def __init__(self,name,age,roll_number):
        self.name=name
        self.age=age
        self.roll_number=roll_number
        
class School:
    def __init__(self):
        self.students=[]
        
    def add_student(self,name,age,roll_number):
        student=Student(name,age,roll_number)
        self.students.append(student)
    
    def display_students(self):
        for student in self.students:
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Roll number: {student.roll_number}")
            print(".................................")
#School object      
school=School()



#menu
while True:
    choice=input("Enter your choice: \n1)Add student \n2)Display list of students \n5)Quit")
    if choice =="1":
        #accepting data from the user
        name=input("Enter name of the Student : ")
        age=input("Enter age : ")
        roll_number=input("Enter roll number : ")
        
        #creating a student object and adding it to the school 
        school.add_student(name,age,roll_number)
    elif choice =="2":
        school.display_students()
        
    elif choice =="5":
        break
        
    
                