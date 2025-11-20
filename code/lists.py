"""
fruit_bag = ['apples', 'bananas']
print(fruit_bag)
fruit_bag.append('Strawberry')
print(fruit_bag)

fruit_bag.extend(["mango", "grape"])
print(fruit_bag)

fruit_bag.insert(2,"orange")
print(fruit_bag)

fruit_bag.insert(len(fruit_bag),"jackfruit")
print(fruit_bag)

exotic_fruits = ["kiwi", 'dragonfly']
print(exotic_fruits)

fruit_bag = fruit_bag + exotic_fruits
print(fruit_bag)

fruit_bag = exotic_fruits + fruit_bag
print(fruit_bag)

fruit_bag = exotic_fruits + ["watermelon"] + fruit_bag
print(fruit_bag)

fruit_bag.remove("kiwi")
print(fruit_bag)

#fruit_bag = [f for f in fruit_bag if (f!= "kiwi" or f!='dragonfly')]
fruit_bag = [f for f in fruit_bag if (f!= "kiwi" and f!='dragonfly')]
print(fruit_bag)

# accessing through index
for i in fruit_bag:
    print(i)

i = 0
while i < len(fruit_bag):
    print(f"I am the {i + 1} variable and item is {fruit_bag[i]}")
    i = i + 1

fruit_bag = [f for f in fruit_bag if f != 'watermelon']
print(fruit_bag)

fruit_bag.extend(["kiwi", "watermelon", "pineapple"])
print(fruit_bag)

# age = 25
# has_license = False
"""

my_list = ["Sahaj", 15, False]
name = my_list[0]
age = my_list[1]

has_license = my_list[-1]
print(f"My name is {name}, my age is {age} and my license status is {has_license}")

my_list[0] = "Siddhanth"
my_list.append("Arthi")
print(my_list)

# my_list.remove('Arthi')
# print(my_list)

# last = my_list.pop()
# print(last)
# print(my_list)

# last = my_list.pop()
# print(last)
# print(my_list)

# del my_list[0]
# print(my_list)

# del my_list[0]
# print(my_list)

# del my_list[0]
# print(my_list)

# del my_list[0]
# my_list = ["Prashanth", 25, age, True, has_license] print(my_list)

my_list.insert(1, "Sahaj")
print(my_list)

my_list.insert(0, "Prashanth")
print(my_list)
