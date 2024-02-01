people=["Jonh","Rob","Mike",123,4,4,6]
print(people)
#accessing
print(people[0])
#negative index
print(people[-1])
# list slicing
print(people[2:-1])
print(people[3:5])
# in e not/

print("Jonh" in people)
print(8 not in people)
# listFunc 
print(len(people))#Size length list
people.insert(1,"Bernardo")#insert element in a list by index
print(people)

people.append(32) #append item in the end of a list
print(people)
people.extend([1992,"January"]) #add multiple item into list widtout nasting list
print(people)

people.remove("Bernardo")#to remove item
people.pop()#remove last item
people.index(32) #check the index number
#max & min
see=[1,2,3,4,5,6]
print(max(see),min(see))
# nestedList
list1=[1,2,3,4,5]
list2=[2345,[23,[23]],]