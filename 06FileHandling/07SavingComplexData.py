def save_user_data():
     name=input("Enter your name : \n")
     email=input("Enter Email : \n")
     contact=input("Enter your contact : \n")
     
     
     user_data=f"Name : {name}\nEmail : {email}\nContact : {contact}"
     with open ("user_data.txt","a") as file:
         file.write(user_data)


def read_user_data():
    with open("user_data.txt","r") as file:
        print(file.read())

     
def UserForm():
    save_user_data()
    read_user_data()