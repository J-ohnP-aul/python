dimensions = (200, 50)
print(dimensions[0])
# dimension[0] = 250
print("\nthe original dimension")
for dimension in dimensions:
    print(dimension)
#overWriting a variable of tuple
#you cant modify a tuple but you can asign new values to the var holding the tutple
dimensions = (400, 100)
print("\nModified tuple")
for dimension in dimensions:
    print(dimension)
