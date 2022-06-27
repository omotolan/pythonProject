def addition(first_number, second_number):
    return first_number + second_number


def subtraction(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def division(first_number, second_number):
    return first_number / second_number


def remainder(first_number, second_number):
    return first_number % second_number


def whole_number(first_number, second_number):
    return first_number // second_number


first_num = 34
second_num = 7

result = addition(first_num, second_num)
print(f"result is {result}")

result = subtraction(first_num, second_num)
print(f"result is {result}")

result = multiply(first_num, second_num)
print(f"result is {result}")

result = division(first_num, second_num)
print(f"result is {result:.2f}")

result = remainder(first_num, second_num)
print(f"result is {result}")

result = whole_number(first_num, second_num)
print(f"result is {result}")
