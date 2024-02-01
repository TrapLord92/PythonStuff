numbers=set([1,2,3,4,5,6])
print(numbers)
alsoset={1,2,3,3,4,5,6}
print(alsoset)
print(alsoset.issuperset(alsoset))
# emptySet
s=set()

setA={1,2,4,5,6,7,3}
setb={10,11,12,13,14,3}
print(setA|setb) #union of set
print(setA & setb)# intersection set
print(setA ^ setb) #remove simetric elements

setA.add(20)
print(setA)
setA.remove(4 )
# if you no certain if element exist in the set use the discard Method
print(setA)
