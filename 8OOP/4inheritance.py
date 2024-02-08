
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
        
        
#digital class inherits everything from Product class   
class Digital_product(Product):
    def __init__(self,link):
        self.link=link
    
    def getlink(self):
        self.link=input("enter product link")
        
    def display_link(self):
        print(self.link)


ebook=Digital_product("")
ebook.get_data()
ebook.getlink()
ebook.put_data()
ebook.display_link()