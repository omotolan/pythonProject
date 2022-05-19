add = lambda x, y: x + y


def add(a, b):
    return a + b


def sub(c, d):
    return d - c


def operate(x, y, func):
    return func(x, y)


val_sub = operate(6, 13, sub)
val_add = operate(6, 13, add)

print(val_add)
print(val_sub)


def multiply(x, y):
    return x * y


val_mul = operate(34, 2, multiply)
print(val_mul)

div = operate(5, 24, lambda x, y: y / x)

print(div)

def multiple(x, func):
    return func(x)

double = multiple(4, lambda x: x * 2)

print(double)
