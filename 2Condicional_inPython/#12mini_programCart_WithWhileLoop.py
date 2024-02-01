cart=[]

while True:
    user_choice=input("Do you wish to add item in the cart ? : \n enter 'enter y for yes'")

    if user_choice == "y":
        item=input("insert an item to the Cart : \n")
        cart.append(item)
        print(f"current cart item are : \n {cart}")
    else:
        break   

