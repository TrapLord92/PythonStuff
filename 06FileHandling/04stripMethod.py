with open('data.txt',"r") as line:
    content1=line.readlines()
   

    
print(content1)
for line in content1:
    print(line.strip())