#methods in oop are  functions declared in the class


class Product:
    
    #constructor'''Data to be used
    
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    #method to work with the data
    def summer_discount(self,discount):
        self.price=self.price-self.price*discount/100
        
        
p1=Product("T-shirt",10)

print(f"{p1.name} is {p1.price}$")
p1.summer_discount(10)
print(f"summer discount is {p1.price} $")

p2=Product("Laptop",1000)
print(f"{p2.name} is {p2.price}$")
p2.summer_discount(20)
print(f"summer discount is {p2.price} $")
