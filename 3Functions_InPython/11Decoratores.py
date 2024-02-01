def decorator(func):
    def wrapper(*args, **kwargs):
        print("wrapper upside")
        func(*args, **kwargs)
        print("wrapper donwside")
        
    return wrapper

@decorator
def chocolate():
    print("Chocolate")
    
    

 

@decorator
def cake(name):
    print(f"{name} cake")
    
chocolate()
cake("mango")

