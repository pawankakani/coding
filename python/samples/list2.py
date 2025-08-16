myList = [25, "John", 34.56]

print("Number of elements in list are :", len(myList))
print("Elements in list are :", myList)

myList.append(10)
print("Elements in list after append are :", myList)

myList.insert(1, 10)
print("Elements in list after insert are :", myList)

myList.remove(10)
print("Elements in list after remove are :", myList)

myList.pop(1)
print("Elements in list after pop are :", myList)

myList.clear()
print("Length of list after clear is :", len(myList))
