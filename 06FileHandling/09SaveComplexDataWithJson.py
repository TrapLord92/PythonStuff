import json
import os

def save_user_data():
    user_list=[]
    
    while True:
        name=input("Enter name(or 'Q' to exit the program): \n")
        if name =='Q':
            break
        email=input("Enter email")
        contact=input("Enter contact")
        
        # creating a dictionary
        user_data={
            "name":name,
            "email":email,
            "contact":contact
        }
        
        user_list.append(user_data)
        
        # preserving old data
    if os.path.exists("user_data.json"):
        with open("user_data.json","r") as file:
            existing_data=json.load(file)
        user_list.extend(existing_data)
        
    with open("user_data.json","w") as file:
            user_son_data=json.dump(user_list,file)
    print("User data saved Successfully")

# save_user_data()

def read_user_data():
    if not os.path.exists("user_data.json"):
        print("no user data found")
        return
    with open("user_data.json","r") as file:
        user_list=json.load(file)
        for user_data in user_list:
            print("Name", user_data["name"])
            print("Email", user_data["email"])
            print("Contact", user_data["contact"])
            print("\n")

# read_user_data()

#update data
def edit_user_data(name):
    if not os.path.exists("user_data.json"):
        print("no user data found")
        return
    with open ("user_data.json",'r') as file:
        user_list= json.load(file)
    user_found=False
    for user_data in user_list:
        if user_data["name"].lower()==name.lower():
            email=input("Enter updated email: \n")
            contact=input("Enter update contact : \n")
            
            user_data["email"]=email
            user_data["contact"]=contact
            user_found=True
            break
    if not user_found:
        print("User not found")
        
        
    with open("user_data.json","w") as file:
        json.dump(user_list,file)
    print("user data updated successfully")


# edit_name=input("Enter name wich you want to edit data:")
# edit_user_data(edit_name)
# read_user_data()


def delete_user_data(name):
    if not os.path.exists("user_data.json"):
        print("no user data found")
        return
    with open ("user_data.json",'r') as file:
        user_list= json.load(file)
    user_found=False
    for user_data in user_list:
        if user_data["name"].lower()==name.lower():
            user_list.remove(user_data)
            user_found=True
            break
    if not user_found:
        print("User not found")
        
        
    with open("user_data.json","w") as file:
        json.dump(user_list,file)
    print("user data deleted successfully")
    
    
    
delete_name=input("Enter name which you want to delete:")
delete_user_data(delete_name)
read_user_data()