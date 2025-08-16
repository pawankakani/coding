numbers = [1,2,2,3,3,3,4,5,6,7,7,7]

# Creating a set usig list
myset1 = set(numbers) ## <1>

print(type(myset1))

print(numbers)
print(myset1)

# Creating a set directly with values
myset2 = {1,2,3,3,4,4,5} ## <2>

print(type(myset2))
print(myset2)

myset2.add(7)
myset2.add(10)
myset2.remove(5)

print(myset2)
