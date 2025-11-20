# def greet():
#     print('Hi there and welcome to function called greet')

def greet(first_name = 'Prashanth', last_name='Ramachandran'):
     print(f'Hi {first_name} {last_name} and welcome to function called greet')
 
def greet1(first_name, last_name='Ramachandran'):
     print(f'Hi {first_name} {last_name} and welcome to function called greet')

# this forms syntax error as ur unknown last_name is the last 
#def greet(first_name = 'Prashanth', last_name):
def greet2(last_name, first_name = 'Siddhanth'):
     print(f'Hi {first_name} {last_name} and welcome to function called greet')

 
def check_weather(temperature):
    if temperature > 30:
        print(f"Temp = {temperature} °C, weather is hot!!")
    else:
        print(f"Temp = {temperature} °C, weather is nice!!")

# greet()
# check_weather(45)
# check_weather(25)

greet(last_name="Ramachandran", first_name= 'Prashanth')
greet()

greet1("Sahaj")
greet2('Iyer')