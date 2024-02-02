while True:
    
    with open("names.txt","a") as file:
        name=input("enter name to be added : \n")
        file.write(name+ '\n')
        choice=input("Do you want to add more names? insert (y=yes or n=no)\n")
        if choice =="n":
            break
    
