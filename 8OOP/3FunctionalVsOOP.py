def product_data():
    productName=input("Enter product name")
    price=input("Enter price name")
    print(productName)
    print(price)
    

product_data()

class Product:
    def __init__(self,productName,price):
        self.product=productName
        self.price=price
    
    def get_data(self):
        self.product=input("enter product name")
        self.price=input("enter a price name")
    
    def put_data(self):
        print(self.product)
        print(self.price)
        
p1=Product("","")
p1.get_data()
p1.put_data()
        
                