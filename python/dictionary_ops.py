# In below dictionary keys are of type string, and values are of type integer
population = {'London': 8980000, 'Washington': 693000, 'Tokyo': 14000000, 'Frankfurt': 753000}

print(population.items())

population.pop('Tokyo')
print("After pop('Tokyo')", population)

population.popitem()
print("After popitem()", population)

print(population.keys())
print(population.values())
