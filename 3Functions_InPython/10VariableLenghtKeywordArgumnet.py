def products(**kwargs):
    for key,value in kwargs.items():
        print(key ,":", value)




products(name="Iphone",price=700)
products(name="ipad",price="400",description="This is an ipad")