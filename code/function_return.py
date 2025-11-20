import statistics

global CURRENT_DISCOUNT_RATE

CURRENT_DISCOUNT_RATE = 0.05


def get_return_amount_after_discount(price: float):
    price = price - price * CURRENT_DISCOUNT_RATE
    return price


price = 100.0
price = get_return_amount_after_discount(price)
print(price)


def get_min_max_avg(numbers: list[float]):
    return min(numbers), max(numbers), statistics.mean(numbers)


def simple_function():
    numbers = [1, 3, 5, 7, 9]
    return numbers


def simple_function1():
    numbers = [1, 3, 5, 7, 9]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number


print(get_min_max_avg([-100.0, 100.001, -1000000.9, 25.98, 0.1, 99999999.099]))
min_mum, max_mum, average = get_min_max_avg(
    [-100.0, 100.001, -1000000.9, 25.98, 0.1, 99999999.099]
)
print(
    f"The values of minimum are {min_mum: .2f} and maximum are {max_mum: .2f} and the average is {average: .2f}"
)
array_from_function = simple_function()
print(array_from_function)

my_first_number, my_last_number = simple_function1()
print(my_first_number, my_last_number)
