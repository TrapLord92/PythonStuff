# def pRint():
#     print("Hello there")


# pRint()

#PassingArguments
def add(a,b):
    print(a+b)

add(1,2)
#keyword arguments

def speed(distance,time):
    print(distance/time)

speed(time=2,distance=100)

#defaultParameter

def area(radius,pi=3.14):
    print(pi*radius*radius)

area(10)

#return value
def area(radius,pi=3.14):
    return(pi*radius*radius)

area1=area(10)
print(area1)
# caling one func into another
# return mutlpes values

def circle(r):
    area=3.14 *r*r
    circumference =2*3.14*r
    return area,circumference


a,b=circle(10)
print(f"area {a}, circumference {b}")
