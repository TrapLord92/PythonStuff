numbers=[1,2,3,4,5,6,7,8,9,10]

def iS_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n% i==0:
            return False
    return True

is_prime=list(filter(iS_prime,numbers))
print(is_prime)