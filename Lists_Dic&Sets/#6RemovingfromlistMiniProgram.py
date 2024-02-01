
def addItem():
    addItem=input("Do you want to add item to the current list ? \n insert 'y' for yes and 'n' for No")

    if addItem =="y":
        userItem = input("please insert your product")
        position=input("after which product do you want to place ? ")
        #adding to a specific index position
        index=product.index(position)
        product.insert(index+1,userItem)
        print(f"You inserted {userItem} to the current list now the Product list item are : \n {product} ")
    else:
        print("Fell Free to Check us out again ")

product=["Phone","t-shert","telephone"]

user=input(f"The current list item are : {product} \n which element do you want to be removed : \n")

if user in  product:
    product.remove(user)
    print(f"you removed {user} from the list")
    print(f"the current list item are : {product}")
    addItem()

else:
    print("item not found")
    print(f"please chose from the  current list item : {product}")
    addItem()

