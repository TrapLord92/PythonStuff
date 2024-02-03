def func():
    counter =0
    while counter <=10:
        yield counter
        counter +=1
        
print(list(func()))

# def func():
#     counter =0
#     while counter <=10: 
#         counter +=1
#         return counter

# print(func())
def evenG(x):
    for i in range(x):
        if i%2==0:
            yield i
            
print(list(evenG(10)))
     
        
        