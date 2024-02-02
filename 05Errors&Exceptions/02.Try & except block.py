n=int(input("enter a number : "))
d=int(input("Enter denominator : "))
result=0

try:
    result=n/d
except ZeroDivisionError:
    print ("Cannot divide a number by zero")
print(result)