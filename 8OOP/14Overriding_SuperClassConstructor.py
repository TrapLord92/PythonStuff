class Parent:
    def __init__(self):
        self.balance=4000
        
    def display_balance(self):
        print(f"Parent's balance is : {self.balance}")
        
        
class Child(Parent):
    def __init__(self):
       self.balance=2000
       
    def display_balance(self):
         print(f"child's balance is : {self.balance}")
        

mike=Child()

mike.display_balance()