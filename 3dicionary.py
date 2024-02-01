people={
    "name":"Bernardo",
    "age":32,
    "Birth-Contry":"Angola"
}
print(people)

# dic operation
#create_dictionary with dict

newlis=dict(
    jonh=34,
    rob=32,
    tim=20
)
print(newlis)
newlis["mike"]=34
print(newlis)

del newlis["tim"]
print(newlis)
#GetMethod
print(newlis.get("jonh"))
#update&Pop
price={"iphone":500,"pc":1000}
newPrice={"iphone":502,"pc":1010,'t-shert':1500}

price.update(newPrice)
print(price)
price2=price.pop('pc')
print(price2)
newPrice2={"iphone":502,"pc":1010,'t-shert':1500}
#item e Keys Method

print(newPrice2.values())#accessing values
print(newPrice2.keys())#accessing keys
print(newPrice2.items())#accessing as key value pair


