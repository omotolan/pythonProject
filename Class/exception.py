def divide(a, b):
    if b == 0:
        raise ValueError("Denominator can not be Zero")
    return a / b
print(divide(4, 5))
try:
    print(divide(5, 0))
except:
    print("wrong value")



num = int(input("Enter the numerator: "))
den = int(input("Enter the denominator: "))

while True:
    try:
        print(divide(num, den))
        break
    except ValueError:
        print("wrong value")
        num = int(input("Enter the numerator: "))
        den = int(input("Enter the denominator: "))