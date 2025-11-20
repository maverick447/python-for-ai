# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!
print(type(empty_set))
print(empty_set)

empty_set.add(4)
print(empty_set)

empty_set.add('a')
print(empty_set)

empty_set.update(["mango", "grape", "orange"])
print(empty_set)

print(type(empty_set))

'''
The order is not guaranteed — Python sets are designed for fast membership tests (e.g., if "apple" in fruits:), not ordering.
'''
# Set with values - both ways work
numbers = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 'a'}
print(type(numbers))
print(numbers)

fruits = set(["apple", "banana", "orange", 'Apple', 'banana'])
print(fruits)

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90, 21, 22]
unique_scores = set(scores)
# {85, 90, 92}
print(unique_scores)

for i in unique_scores:
    print(i)

colors = {"red", "blue", "yellow"}

# Add items
colors.add("green")
print(colors)  # {'red', 'blue', 'green'}

# Remove items
colors.remove("blue")    # Error if not found
#colors.remove('blue')
colors.discard("yellow") # No error if not found

# # Check membership
# if "red" in colors:
#     print("Red is available")