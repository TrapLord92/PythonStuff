class Product:
    #constructors ;where we declare an initialize property=variable's
    def __init__(self,name,price):
        self.name=name
        self.price=price
        

p1=Product("iphone",200)
p2=Product("laptop",400)

print(p1.name,":",p1.price)
print(p2.name,":" ,p2.price)
        