names=["john Doe","Alice Smith","Bob Ford"]
for name in names:
    print(name.split()[0][0] + name.split()[1][0])
    

# with Map

initialValues=list(map(lambda name: "".join([n[0] for n in name.split()]),names))
print(initialValues)