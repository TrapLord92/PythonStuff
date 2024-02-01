age=(int(input("enter your age : \n")))


if age >=18:
    score=int(input("enter your exam score :\n 18"))
    if score >=45:
        print("You meet both the age and score criteria, you are qualified")
    else:
        print("You meet the age criteria but do not meet the score")
else:
    print("You don't  meet the age criteria please try again when you are above 18")