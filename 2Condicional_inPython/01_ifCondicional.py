# age=15

# if age >=18:
#     print("You are an adult")
# else:
#     print("Welcome back in a few years")

#AcceptingUserData
DATA={"Adult":"You are an adult", "minor":"welcome back i few years","oldAge":"You are a living bibliotheca thank you for your knowledge"}


age=int(input("enter your age : "))

if age ==18:
    print(DATA.get("Adult"))
elif age >= 60:
    print(DATA.get("oldAge"))
elif age < 18 and age > 10:
    print(DATA.get("minor"))
else:
    print("I can't identifier who are you ")
    