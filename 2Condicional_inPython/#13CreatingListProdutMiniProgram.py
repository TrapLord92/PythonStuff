products=[{"name":"iphone","price":500,"description":"the new telephone"},
         {"name":"pc","price":1000,"description":"the new pc"}]

cart=[]

while True:
    choice=input("Do you want to continue Shopping : ? /n (enter yes or no) " )
    if choice == "yes":
        print(f"The current product list is :")
        for index, product in enumerate(products):
            print(f"{index} : name :{product['name']} | price - {product["price"]} | description: {product["description"]}")
            product_id=int(input("enter the id of the product you want to add to the cart"))
            if products[product_id] in cart:
                products[product_id]['quantity'] +=1

            else:
                products[product_id]['quantity']=1
                cart.append(products[product_id])

            total=0
            print(f"Current cart contents are ")

            for product in cart:
                print (f"{product["name"]}: {product['price']} : QTY : { product["quantity"]}")
            total=total +product["price"]*product['quantity']
        print(f"Cart total is : $ {total}")


            
    else:
        break 
print(f"Thank you you final cart content are {cart} and your total amount to pay  is {total}")
