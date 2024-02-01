product={"Phone":800,"t-shirt":100,"telephone":1000}

welcome=input(f"welcome to the store what do you which to do ? \n a=check price , b= add items,c = delete product, or d=to update price : \n")

if welcome == "a":
    print(product)
    user=input(" enter product to check the price ")
    # print value
    print(f'the price of {user} is : {product[user]}')
elif welcome =="b":

    new_product=input("enter the item you wish to add")
    price=input(f"enter the price for {new_product}")
    product[new_product]=price
    print(f"You added {new_product} with price of {price} $ , the current list updated is : \n {product}")

elif welcome =="c":
    print(product)
    user_item_del=input(" enter product to be deleted : \n")

    del product[user_item_del]
    print(f"You deleted {user_item_del} from the list , the updated item list is : { product}")
elif welcome =="d":
    print(product)
    itemUpdate=input("you want to update :\n 1=price or 2=item & price")
    if itemUpdate == "1":

        user_price_update=input(" enter product to be updated : \n")
        newPrice=input(f"Enter the new price for {user_price_update}")
        product[user_price_update]=newPrice
        print(f"You updated the price {user_price_update} from the list , the updated item list is : { product}")

    elif itemUpdate =="2":
        user_price_update=input(" enter product to be updated : \n")
        newPrice=input(f"Enter the new price for {user_price_update}")
        item_name=input("Enter the item name you want to update")
        new_name=input(f"Enter the new name of {item_name}")
        product[item_name]=new_name
        product[user_price_update]=newPrice
        print(f"Item sucessfully  updated item list is : { product}")




else:
    print("please insert a valid command")




