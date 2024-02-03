numbers=[1,3,4,5,6,7]
oddNum=[]

for num in numbers:
    if num%2==1:
        oddNum.append(num)
    
print(f"The odd numbers are :\n {oddNum}")

#with filter

def odd(x):
    if x%2==1:
        return x
odd_num=(list(filter(odd,numbers)))
print(odd_num)

# with lambda
odd_num=(list(filter(lambda x:x%2==1,numbers)))
print(odd_num)

