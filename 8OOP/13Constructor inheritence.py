class Parent:
    def __init__(self):
        self.balance=4000
        
    def display_balance(self):
        print(f"Parent's balance is : {self.balance}")
        
        
class Child(Parent):
    pass

mike=Child()

mike.display_balance()