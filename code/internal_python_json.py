import json

person = {
    "name": "Alex",
    "age": 25,
    "city": "San Jose",
    "languages": ["Python", "C", "C++"]
}

# Convert to JSON string
json_dict = json.dumps(person, indent=4, sort_keys=True)
print(json_dict)
print(type(json_dict))

dict_from_str = json.loads(json_dict)
print(json_dict)
print(type(dict_from_str))

both_in_out_dicts_are_equal = (person == dict_from_str)
print(f'person vs dict_from_str ? {both_in_out_dicts_are_equal}')

# File dumping 
with open('dict_to_text.txt', 'w') as file:
    json.dump(person, file, indent=4, sort_keys=True)

dict_from_str = ""
# reading a file 
with open('dict_to_text.txt', 'r') as file:
    dict_from_str = json.load(file)
    
print(dict_from_str)

both_in_out_dicts_are_equal = (person == dict_from_str)
print(f'person vs dict_from_str ? {both_in_out_dicts_are_equal}')
