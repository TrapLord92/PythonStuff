while True:
    
    with open("names.txt","a") as file:
        name=input("enter name to be added : \n")
        file.write(name+ '\n')
        choice=input("Do you want to add more names? insert (y=yes or n=no)\n")
        if choice =="n":
            break
with open("names.txt","r")as file:
    lines=file.readlines()


# print(line.strip().capitalize()) 
#Code to save clean data   
for line in lines:
    with open("clean.txt","a") as clean:
        clean_data=(line.strip().capitalize())  
        clean.write(clean_data+ "\n")
    