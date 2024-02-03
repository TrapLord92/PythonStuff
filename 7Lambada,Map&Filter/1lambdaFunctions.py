# normal function
def square(x):
    return x**2


print(square(2))

#lambda func
result=(lambda x: x**2)(2)

print(result)

add=(lambda x,y:x+y)(1,2)
defaultArg=(lambda x=10,y=20:x+y)
print(defaultArg)
defaultArg=(lambda y,x=10:x+y)(y=40)
print(defaultArg)
print(add)
