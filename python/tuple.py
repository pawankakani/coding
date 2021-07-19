# Use round brackets and comma separated values to declare a tuple
daysOfWeek = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat') ## <1>

# Another way to declare a tuple
tenses = tuple(['Past', 'Present', 'Future'])

print("Values in daysOfWeek are ", daysOfWeek)
print("Values in tenses are ", tenses)

# Accessing 4th element of tuple, note that index starts from zero
print("4th day of week is ", daysOfWeek[3])

# Adding a new value to tuple will not work
# daysOfWeek.append('test') ## <2>

