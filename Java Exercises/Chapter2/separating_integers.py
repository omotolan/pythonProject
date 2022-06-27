print("Separating numbers")

number = int(input("Enter a four digit number: "))

first_number = number % 10
second_number = (number % 100) // 10
third_number = (number % 1000) // 100
forth_number = (number // 1000)

print(first_number)
print(second_number)
print(third_number)
print(forth_number)
