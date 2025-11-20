# Empty tuple
empty = ()
print(empty)
# Tuple with items
point = (3, 5, 9)
colors = ("red", "green", "blue")
print(f"{point} {colors}")
# Single item tuple needs comma!
single = (42,)  # Note the comma
print(single)
not_tuple = 42  # This is just 42 in parentheses
print(type(not_tuple))
print(not_tuple)


# Without parentheses (implicit)
coordinates = 10, 20
print(coordinates)
print(type(coordinates))

for i in point:
    print(i)

# more c like , and in python the paradigm changes
# but still
i = 0
while i < len(point):
    print(point[i])
    i = i + 1

# Unpack values
# point = (3, 5)
x, y, z = point  # x = 3, y = 5
print(x, y, z)
print(type(x))

# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)
print(a, b, c)
print(type(a))

# Swap variables elegantly
x, y, z = z, x, y  # Swaps values!
print(x, y, z)
