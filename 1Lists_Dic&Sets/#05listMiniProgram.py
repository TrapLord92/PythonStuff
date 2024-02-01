product=["Phone","t-shert","telephone"]
p="string"


item=input("Enter Product to search : \n")
item=item

if item in product:
    print(f"The product {item} you search ,exist in this database ")
else:
    print(f"the {item} you searched don't exist in this database")