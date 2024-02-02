# file=open("data.txt","w")#append mode w- will rewrite the file destinetion
file=open("data.txt","a") #will append data to file destinection
content="\n1another new line"
file.write(content)
file.close()