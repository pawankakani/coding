myList = [25, "John", 34.56, ['a', 2, 10]] ## <1>

print(type(myList))

# use index 1 for second element
print("The second element of list is :", myList[1]) ## <2>

# access nested list in similar fashion
# first reach out to nested list, then the element within it
print("First element of nested list is :", myList[3][0]) ## <3>
