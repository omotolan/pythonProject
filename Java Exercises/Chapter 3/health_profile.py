import datetime


class HealthProfile:
    year = datetime.datetime.now()

    def __init__(self, first_name, last_name, day_of_birth,
                 month_of_birth, year_of_birth, weight, height, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.day_of_birth = day_of_birth
        self.month_of_birth = month_of_birth
        self.year_of_birth = year_of_birth
        self.weight = weight
        self.height = height
        self.gender = gender

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_weight(self, weight):
        if (weight <= 0):
            print("weight can not be less than or equal to 0")
        self.weight = weight

    def set_height(self, height):
        if(height <= 0):
            print("height can not be less than or equal to 0")
        self.height = height

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height

    def get_age(self):
        return int(self.year.year) - int(year_of_birth)


first_name = input("Enter your first name: ")
last_name = input("Enter you last name: ")
day_of_birth = input("Enter day of birth: ")
month_of_birth = input("Enter month of birth: ")
year_of_birth = input("Enter year of birth: ")
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
gender = input("Enter gender: ")

patient_one = HealthProfile(first_name, last_name, day_of_birth, month_of_birth, year_of_birth, weight, height, gender)


def calculate_bmi():
    return patient_one.get_weight() * (patient_one.height * patient_one.height)


def max_hearth_rate():
    return 220 - int(patient_one.get_age())


bmi = calculate_bmi()
print("your bm is " + str(bmi))

max_hearth_rate = max_hearth_rate()
print("your max heart rate is: " + str(max_hearth_rate))

print(patient_one.__dict__)
