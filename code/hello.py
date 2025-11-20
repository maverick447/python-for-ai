# snake-case is preferred by Python 
# camelCase isn't 

first_name = "Jane"
last_name = "Doe"
hello = 'Hello! ' * 4
# Using +
full_name = first_name + " " + last_name  # "Jane Doe"
print(full_name)
# Using f-strings (modern Python way!)
greeting = f"{hello}, {first_name}!"  # "Hello, Jane!"
print(greeting)
# Multiple variables
age = 25
intro = f"I'm {first_name} and I'm {age} years old"
print(intro)

intro = intro.lower()
print(intro)

intro = intro.upper()
print(intro)

intro = intro.title()
print(intro)

# this prints a floor() operation 
print(19 // 5)

for i in range(0,101,5):
    print(i)
    
name = "Python"
for i in name:
    print(i)
    

for i in range(0, len(name), 2):
    print(name[i])