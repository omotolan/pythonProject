def calculate_bmi(weight, height):
    return weight / (height * height)


print("calculate your body mass index")
weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

print(f"your body mass index is: {bmi:.2f}")
print("BMI Values")
print("underweight: less than 18.5")
print("normal: between 18.5 and 24.9")
print("overweight: between 25 and 29.9")
print("obese: 30 or greater")
