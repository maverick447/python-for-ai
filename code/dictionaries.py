person = {}
person = {
    "name" : "Prashant",
    "age": 25,
    "city": 'Boston'  
}

print(person)
print(person["age"])
print(person["city"])

# iteration over keys 
key_number = 1
for key in person.keys():
    print(f'key-{key_number}: {key}' )
    key_number = key_number + 1
    
# iteration over values 
value_number = 1
for value in person.values():
    print(f'value-{value_number}: {value}' )
    value_number = value_number + 1

# together 
key_number = 1
value_number = 1
for key, value in person.items():
    print(f'Key{key_number} = {key} and Value{value_number} = {value}')
    key_number = key_number + 1
    value_number = value_number + 1

person["name"] = 'Sahaj'
    
# to add a value 
##person.append({"name": "Sahaj", "age":15, 'city': 'San Antonio'})
# there no method to do it by calling append
all_people = [
    {"name" : "Prashant", "age": 25, "city": 'Boston'},
    {"name": "Sahaj", "age":15, 'city': 'San Antonio'}
     
] 
print(all_people)
print("*")
print(all_people[1])
print('*')
# all_people1_dict = {
#     {"name-1" : "Prashant", "age": 25, "city": 'Boston'},
#     {"name-2": "Sahaj", "age":15, 'city': 'San Antonio'}
# }

#print(all_people1_dict)     
person["has_license"] = True
print(person)

print(person.keys())
print(type(person.keys))
array = []
array += person.keys()
print(array)

array.clear()
array += person.values()
print(array)

array = person.items()
print(type(array))
print(array)
print(array[3])

