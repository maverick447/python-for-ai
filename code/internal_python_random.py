import random

total_numbers  = random.randint(10, 20)
array = []
#print(array)

for i in range(0,total_numbers+1):
    array.append(random.randint(-1000,1000))
    print(i, array[i])

print(array)    

magical_number = random.choice(array)
print(f'Out of {len(array)} we have {magical_number} as the luckiest!!')
array_fruits = ['apple', 'banana', 'orange']
print(f'out the following fruits {array_fruits} the magical fruit is {random.choice(array_fruits)}')