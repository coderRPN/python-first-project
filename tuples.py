# tuples are immutable lists

coordinates = (4, 5)

print("Coordinates at 0: " + str(coordinates[0]))

# coordinates[0] = 2 no can't do

# create tuple of tuples

coordinates = ((5, 4), (9, 6), (22, 11))

print("tuple of tuple coordinates: " + str(coordinates))
# coordinates[0] = (3, 3) can't do
# coordinates[0][0] = 55; can't do

# create list of tuples
coordinates = [(5, 4), (9, 6), (22, 11)]
print("list of tuple coordinates: " + str(coordinates))

coordinates[0] = (3, 3)
print("Change 0th tuple in list to (3,3): " + str(coordinates))
# coordinates[0][0] = 55; can't do


