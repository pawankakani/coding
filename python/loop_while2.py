myList = [10, 20, 30, 40, 50]

# Variable to check loop condition
list_index = 0
while list_index < len(myList): ## <1>
    print(myList[list_index])
    list_index = list_index + 1

print("Loop has finished") ## <3>
