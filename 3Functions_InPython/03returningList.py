def remove_duplicates(numbers):
    newList=[]
    for number in numbers:
        if number not in newList:
            newList.append(number)
    return newList

def removeByset(numbers):
    return list(set(numbers))


ids=[1,1,2,2,2,3,3,4,4,4,5,5,5]

newList=remove_duplicates(ids)
setList=removeByset(ids)

print(newList)
print(setList)