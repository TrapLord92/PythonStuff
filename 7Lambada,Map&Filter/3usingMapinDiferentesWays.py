numbers=["1","2","3","4","5"]

# converting string values to int values
new=list(map(int,numbers))
print(new)

prices=[100,200,300,400,500]

# func descont 5% with lambda func
new_prices=list(map(lambda x:x-x*5/100,prices))
print(new_prices)
#capitalize string
names=["domingos","bernardo"]

cap_names=list(map(str.capitalize,names))
print(cap_names)
