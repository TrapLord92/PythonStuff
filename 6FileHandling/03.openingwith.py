# with open('data.txt',"r") as file:
#     content=file.read()
#     print(content)
    
    
with open('data.txt',"r") as line:
    content1=line.readlines()
    
print(content1)
for line in content1:
    print(line)