n=int(input("enter a number : "))
d=int(input("Enter denominator : "))

try:
    result=n/d
except ZeroDivisionError:
    print ("Cannot divide a number by zero")
else:
    print(result)